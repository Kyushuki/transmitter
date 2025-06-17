from encoder.coder.coder import Coder
from encoder.coder.my_encoder import MyEncoder

import json

file = 'my_code.json'

with open(file, 'r', encoding='UTF-8') as f:
    code = json.load(f)

test_Coder = Coder()
test_My = MyEncoder(code)

def test_encode():
    assert test_Coder.encode("Привет!") == "11001111111100001110100011100010111001011111001000100001"
def test_myencode():
    assert test_My.encode("fff") == 3*"111111"