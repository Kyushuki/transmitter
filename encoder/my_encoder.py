from coder import Coder

class MyEncoder(Coder):
    """
    Класс реализует кодировку сообщений в собственной кодировке

    Параметры:

    alphabet: dict - словарь с необходимой кодировкой вида (символ-код)
    """
    def __init__(self,alphabet: dict):
        self.code = alphabet

    def encode(self,mess: str) -> str:
        """
        Метод принимает на вход текстовое сообщение и кодирует его согласно кодировке собственной в my_code.json

        ВНИМАНИЕ:

        Кодировка поумолчанию не предполагает заглавных букв и многих знаков препинания

        Если символа нет в кодировке, он будет заменён на "#" = "111111"

        Параметры:

        mess: string

        Возвращает - string
        """
        res = ""
        for i in mess:
            try:
                res+= self.code[i]
            except KeyError:
                res+=self.code["#"]
        return res 
