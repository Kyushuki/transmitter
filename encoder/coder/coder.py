class Coder():
    def __init__(self):
        pass
    def encode(self,mess: str) -> str:
        """
        Метод использует windows-1251 для кодировки "алфавит-биты"

        Параметры:

        mess: string

        Возвращает - string
        """
        return "".join(f"{i:08b}" for i in mess.encode("windows-1251"))
