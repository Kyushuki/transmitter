from encoder.coder.coder import Coder
from encoder.coder.my_encoder import MyEncoder


def test_encode():
    test_Coder = Coder()

    assert test_Coder.encode("Привет!") == "11001111111100001110100011100010111001011111001000100001"
    assert test_Coder.encode("123456,789") == "00110001001100100011001100110100001101010011011000101100001101110011100000111001"
    assert test_Coder.encode("abcd") == "01100001011000100110001101100100"


def test_myencode():
    import json

    file = 'my_code.json'

    with open(file, 'r', encoding='UTF-8') as f:
        code = json.load(f)
    test_My = MyEncoder(code)

    assert test_My.encode("fff") == 3 * "111111"
    assert test_My.encode("абетка") == "000000000001000101010011001011000000"
    assert test_My.encode("Коро") == "111111001111010001001111"
    assert test_My.encode("123456789") == "100001100010100011100100100101100110100111101000101001"
    assert test_My.encode("два") == "000100000010000000"
    assert test_My.encode(", ") == "101101101010"
