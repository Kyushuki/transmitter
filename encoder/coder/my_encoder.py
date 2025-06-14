import json 
import os 
from coder import Coder

file = 'my_code.json'

with open(file, 'r', encoding='UTF-8') as f:
    code = json.load(f)

class MyEncoder(Coder):
    def encode(self,mess: str) -> str:
        """
        Метод принимает на вход текстовое сообщение и кодирует его согласно кодировке заданной в my_code.json

        ВНИМАНИЕ:

        Кодировка по умолчанию не предполагает заглавных букв и многих знаков препинания

        Если символа нет в кодировке, он будет заменён на "#" = "111111"

        Параметры:

        mess: string

        Возвращает - string
        """
        res = ""
        for i in mess:
            try:
                res+= code[i]
            except KeyError:
                res+=code["#"]
        return res 
