from decoder.coder.decoder import Decoder
from decoder.coder.my_decoder import MyDecoder


def test_decoder():
    D = Decoder()
    d = {
        "11001111111100001110100011100010111001011111001000100001": "Привет!",
        "00110001001100100011001100110100001101010011011000101100001101110011100000111001": "123456,789",
        "01100001011000100110001101100100": "abcd"
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
