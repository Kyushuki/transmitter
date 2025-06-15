from demodulate import Demodulate
from depacket import DePacket

modulator = Demodulate()


depacket = DePacket()

mess=[]
dem_mess = modulator.demodulate(mess)
dpacket, c = depacket.depacket(dem_mess)

if c == "basic":
    from coder.decoder import Decoder
    decoder = Decoder()
elif c == "mycode":
    from coder.my_decoder import MyDecoder
    import json

    file = 'my_code.json'

    with open(file, 'r', encoding='UTF-8') as f:
        code = json.load(f)

    decoder = MyDecoder(code)

mess_decoded = decoder.decode(dpacket)
print(f'Демодулированное\n{dem_mess}\nОтброшены пакетные части\n{dpacket}\nДекодированное сообщение\n{mess_decoded}')