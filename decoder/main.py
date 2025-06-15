from coder.my_decoder import MyDecoder
from demodulate import Demodulate
import json

file = 'my_code.json'

with open(file, 'r', encoding='UTF-8') as f:
    code = json.load(f)

modulator = Demodulate()
decoder = MyDecoder(code)

mess = []
d_mess = modulator.demodulate(mess)
decoded = decoder.decode(d_mess)
print(decoded)