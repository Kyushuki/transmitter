from input import Input
from coder.my_encoder import MyEncoder
# from coder.coder import Coder
from modulate import Modulate

key = Input()
coder = MyEncoder()
# coder = Coder()
modulator = Modulate()

mess = key.input()
newMess = coder.encode(mess)
modulateMess = modulator.modulate(newMess)
print(f'{newMess} \n {modulateMess}')