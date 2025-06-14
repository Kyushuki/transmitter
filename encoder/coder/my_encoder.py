import json 
import os 


nameCode = 'my_code.json'
dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(dir,nameCode)
with open(file, 'r', encoding='UTF-8') as f:
    code = json.load(f)

def encode(mess: str):
    res = ""
    for i in mess:
        res+= code[i]
    return res 
print(encode("привет! как дела?"))