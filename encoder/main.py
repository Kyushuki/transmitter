from input import Input
from modulate import QPSKModulate
from packet import Packet


key = Input()


modulator = QPSKModulate()
packet = Packet()

mess, c = key.input()
if c == "mycode":
    import json

    file = 'my_code.json'

    with open(file, 'r', encoding='UTF-8') as f:
        code = json.load(f)

    from coder.my_encoder import MyEncoder
    coder = MyEncoder(code)
elif c == "basic":
    from coder.coder import Coder
    coder = Coder()

newMess = coder.encode(mess)
packeded = packet.pack(newMess, c)
modulateMess = modulator.modulate(packeded)
print(f'Закодированное сообщение:\n{newMess}\nУпакованное:\n{packeded}\nМодулированное:\n{modulateMess}')
