class Decoder():
    """
    Стандартный класс декодировки
    """
    def decode(self, mess: str) -> str:
        """
        Метод декодирует из windows-1251 в алфавит
        """
        b = [int(mess[i:i + 8], 2) for i in range(0, len(mess), 8)]
        b = bytes(b)
        return b.decode("windows-1251")
