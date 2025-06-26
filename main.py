from encoder.modulate import Modulate
from decoder.demodulate import Demodulate
from encoder.input import Input


class Model:

    def __init__(self):
        self.modulator = Modulate()
        self.demodulator = Demodulate()
        self.input = Input()
        self.mess = ""
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

    def emitter(self):
        self.mess, self.coder = self.input.input()
        if self.coder == "mycode":
            from encoder.coder.my_encoder import MyEncoder
            code = self.import_coder(self.file)
            self.coder = MyEncoder(code)
        else:
            from encoder.coder.coder import Coder
            self.coder = Coder()
        byte_mess = self.coder.encode(self.mess)
        complex_mess = self.modulator.modulate_qpsk(byte_mess)
        return complex_mess


if __name__ == "__main__":
    model = Model()
    print(model.emitter())
