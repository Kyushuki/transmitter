from input import Input
from coder.my_encoder import MyEncoder
# from coder.coder import Coder
from modulate import QPSKModulate
import json

file = 'my_code.json'

with open(file, 'r', encoding='UTF-8') as f:
    code = json.load(f)

key = Input()
coder = MyEncoder(code)
# coder = Coder()
modulator = QPSKModulate()

mess = key.input()
newMess = coder.encode(mess)
modulateMess = modulator.modulate(newMess)
print(f'{newMess} \n {modulateMess}')