from encoder.modulate import Modulate
from decoder.demodulate import Demodulate
from encoder.input import Input
from encoder.packet import Packet
from decoder.depacket import DePacket
import numpy as np
import matplotlib.pyplot as plt


class Model:

    def __init__(self, file: str, beta: float, mean: float, sigma: float):
        self.modulator = Modulate()
        self.demodulator = Demodulate()
        self.input = Input()
        self.packing = Packet()
        self.depacking = DePacket()
        self.coder = ""
        self.file = file
        self.beta = beta  # коэфф затухания
        self.mean = mean
        self.sigma = sigma

    def import_coder(self, file: str) -> dict:
        # file - название файла .json
        import json

        with open(file, 'r', encoding='UTF-8') as f:
            code = json.load(f)
        return code

    def start_signal_phase(self) -> complex:
        phi = np.random.uniform(0, 2 * np.pi)
        phase = np.exp(1j * phi)
        return complex(phase)

    def emitter(self) -> list[complex]:
        mess, self.coder = self.input.input()
        code_for_packet = self.coder
        if self.coder == "mycode":
            from encoder.coder.my_encoder import MyEncoder
            code = self.import_coder(self.file)
            self.coder = MyEncoder(code)
        else:
            from encoder.coder.coder import Coder
            self.coder = Coder()
        byte_mess = self.coder.encode(mess)
        packed_mess = self.packing.pack(byte_mess, code_for_packet)
        complex_mess = self.modulator.modulate_qpsk(packed_mess)

        plt.scatter(np.array(complex_mess).real, np.array(complex_mess).imag, color='violet', label='эталон')

        r = self.start_signal_phase()
        complex_mess = [c * r for c in complex_mess]
        plt.scatter(np.array(complex_mess).real, np.array(complex_mess).imag, color='red', label='с поворотом')

        complex_mess = [c * self.beta for c in complex_mess]
        plt.scatter(np.array(complex_mess).real, np.array(complex_mess).imag, color='blue', label='с затуханием')

        for i in range(len(complex_mess)):
            complex_mess[i] += np.random.normal(self.mean, self.sigma) + 1j * np.random.normal(self.mean, self.sigma)
        plt.scatter(np.array(complex_mess).real, np.array(complex_mess).imag, color='green', label='с шумом', marker='*')

        return complex_mess

    def receiver(self, complex_mess: list[complex]):
        counter = 0
        packed_mess = self.demodulator.demodulate_qpsk(complex_mess)
        byte_mess, coder = self.depacking.depacket(packed_mess)
        if coder == "error":
            while coder == "error":
                packed_mess = self.demodulator.demodulate_qpsk(complex_mess)
                byte_mess, coder = self.depacking.depacket(packed_mess)
                if counter >= 100:
                    return "ОШИБКА, неудалось расшифровать сообщение"
        if coder == "mycode":
            print("Используемая кодировка для расшифровки - mycode\n")
            from decoder.coder.my_decoder import MyDecoder
            code = self.import_coder(self.file)
            coder = MyDecoder(code)
        else:
            print("Используемая кодировка для расшифровки - basic\n")
            from decoder.coder.decoder import Decoder
            coder = Decoder()
        mess = coder.decode(byte_mess)
        return mess


if __name__ == "__main__":
    model = Model('my_code.json', 0.5, 0, 0.1)
    a = model.emitter()
    print(a)
    b = model.receiver(a)
    print(f"Получено сообщение:\n {b}")
    plt.grid(True, linestyle="--")
    plt.axhline(0, 0, color='black', linewidth=0.4)
    plt.axvline(0, 0, color='black', linewidth=0.4)
    plt.title("Созвездие сигнала от передатчика")
    plt.legend()
    plt.show()
