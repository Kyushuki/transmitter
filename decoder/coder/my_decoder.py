class MyDecoder():
    """
    Класс декодера для собственного кода

    Параметры:

    code: dict - словарь с необходимой кодировкой вида (символ-код)

    При инициализации экземпляр создает обратный словарь из полученного на вход
    """
    def __init__(self, code: dict):
        self.rCode = {v: k for k, v in code.items()}
        self.k = len(next(iter(self.rCode)))

    def decode(self, mess: str) -> str:
        """
        Метод декодирует биты в символы собственной кодировки

        Параметры:

        mess: string

        Возвращает декодированное сообщение string
        """
        res = ""
        for i in range(0, len(mess), self.k):
            part = mess[i:i + self.k]
            if part in self.rCode:
                res += self.rCode[part]
            else:
                res += "#"
        return res
