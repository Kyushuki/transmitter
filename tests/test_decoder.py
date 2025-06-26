from decoder.coder.decoder import Decoder
from decoder.coder.my_decoder import MyDecoder


def test_decoder():
    D = Decoder()
    d = {
        "110011111111000000100001": "Пр!",
        "001100010011001000110011": "123",
        "0110000101100010": "ab"
    }
    for k, v in d.items():
        assert D.decode(k) == v


def test_mydecoder():
    import json

    file = 'my_code.json'

    with open(file, 'r', encoding='UTF-8') as f:
        code = json.load(f)
    D = MyDecoder(code)
    d = {
        "111111001111010001001111": "#оро",
        "101101101010": ", ",
        "000100000010000000": "два"
    }
    for k, v in d.items():
        assert D.decode(k) == v
