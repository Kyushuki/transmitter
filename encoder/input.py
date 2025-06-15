class Input():
    """
    Класс реализации ввода сообщений
    """
    def input(self) -> tuple:
        """
        Метод для ввода сообщений
        """
        while True:
            code = input("Введите желаемую кодировку (basic or mycode): ")
            if code.strip() and (code.strip()== "basic" or code.strip()=="mycode"):
                break
            else:
                print("Ошибка: поле не может быть пустым!") 
        while True:
            mess = input("Введите сообщение: ")
            if mess.strip():
                break
            else:
                print("Ошибка: сообщение не может быть пустым!") 
        return mess, code.strip()