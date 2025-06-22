class MyDecoder():
    """
    Класс декодера для собственного кода

    Параметры:

    code: dict - словарь с необходимой кодировкой вида (символ-код)

    При инициализации экземпляр создает обратный словарь из полученного на вход
    """
    def __init__(self, code: dict):
        self.rCode = {v: k for k, v in code.items()}

    def decode(self, mess: str) -> str:
        """
        Метод декодирует биты в символы собственной кодировки

        Параметры:

        mess: string

        Возвращает декодированное сообщение string
        """
        res = ""
        for i in range(len(mess), 6):
            part = mess[i:i + 6]
            if part in self.rCode:
                res + self.rCode[part]
            else:
                res += "#"
        return res
