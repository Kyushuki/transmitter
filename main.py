from encoder.modulate import Modulate
from decoder.demodulate import Demodulate
from encoder.input import Input
from encoder.packet import Packet
from decoder.depacket import DePacket


class Model:

    def __init__(self):
        self.modulator = Modulate()
        self.demodulator = Demodulate()
        self.input = Input()
        self.packing = Packet()
        self.depacking = DePacket()
        self.coder = ""
        self.file = 'my_code.json'

    def import_coder(self, file: str) -> dict:
        # file - название файла .json
        import json

        with open(file, 'r', encoding='UTF-8') as f:
            code = json.load(f)
        return code

    def start_signal_phase(self):
        pass

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
        return complex_mess

    def receiver(self, complex_mess: list[complex]):
        packed_mess = self.demodulator.demodulate_qpsk(complex_mess)
        byte_mess, coder = self.depacking.depacket(packed_mess)
        if coder == "mycode":
            from decoder.coder.my_decoder import MyDecoder
            code = self.import_coder(self.file)
            coder = MyDecoder(code)
        else:
            from decoder.coder.decoder import Decoder
            coder = Decoder()
        mess = coder.decode(byte_mess)
        return mess


if __name__ == "__main__":
    model = Model()
    a = model.emitter()
    print(a)
    b = model.receiver(a)
    print(b)
