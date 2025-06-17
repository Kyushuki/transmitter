from encoder.coder import Coder
from encoder.my_encoder import MyEncoder

import json

file = 'my_code.json'

with open(file, 'r', encoding='UTF-8') as f:
    code = json.load(f)

test_Coder = Coder()
test_My = MyEncoder(code)

def test_encode():
    assert not test_Coder.encode("111") == "###"
def test_myencode():
    assert test_My.encode("fff") == 3*"111111"