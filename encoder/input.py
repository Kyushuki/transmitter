class Input():
    """
    Класс реализации ввода сообщений
    """
    def input(self) -> tuple:
        """
        Метод для ввода сообщений
        """
        while True:
            code = input("Введите желаемую кодировку (basic или mycode) \nИли нажмите ENTER для использования кодировки по-умолчанию(basic): ")
            if code.strip() and (code.strip() == "basic" or code.strip() == "mycode"):
                break
            elif code.strip() and (code.strip() != "basic" or code.strip() != "mycode"):
                print("Ошибка: введите правильную кодировку!")
            else:
                code = "basic"
                break
        while True:
            mess = input("Введите сообщение: ")
            if mess.strip():
                break
            else:
                print("Ошибка: сообщение не может быть пустым!")
        return mess, code.strip()
