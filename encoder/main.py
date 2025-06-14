from input import Input
# from coder.my_encoder import MyEncoder
from coder.coder import Coder
from modulate import QPSKModulate

key = Input()
# coder = MyEncoder()
coder = Coder()
modulator = QPSKModulate()

mess = key.input()
newMess = coder.encode(mess)
modulateMess = modulator.modulate(newMess)
print(f'{newMess} \n {modulateMess}')