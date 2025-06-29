class Coder():
    """
    Класс кодировки алфавита в биты с windows-1251

    Является классом поумолчанию
    """
    def encode(self, mess: str) -> str:
        """
        Метод использует windows-1251 для кодировки "алфавит-биты"

        Параметры:

        mess: string

        Возвращает - string
        """
        return "".join(f"{i:08b}" for i in mess.encode("windows-1251"))
