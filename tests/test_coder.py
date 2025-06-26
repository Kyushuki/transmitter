from encoder.coder.coder import Coder
from encoder.coder.my_encoder import MyEncoder


def test_encode():
    test_Coder = Coder()

    assert test_Coder.encode("Пр!") == "110011111111000000100001"
    assert test_Coder.encode("12") == "0011000100110010"
    assert test_Coder.encode("abc") == "011000010110001001100011"


def test_myencode():
    import json

    file = 'my_code.json'

    with open(file, 'r', encoding='UTF-8') as f:
        code = json.load(f)
    test_My = MyEncoder(code)

    assert test_My.encode("ff") == 2 * "111111"
    assert test_My.encode("абе") == "000000000001000101"
    assert test_My.encode("Кор") == "111111001111010001"
    assert test_My.encode("12") == "100001100010"
    assert test_My.encode(", ") == "101101101010"
