class Input():
    """
    Класс реализации ввода сообщений
    """
    def input(self) -> str:
        """
        Метод для ввода сообщений
        """
        while True:
            mess = input("Введите сообщение: ")
            if mess.strip():
                return mess
            else:
                print("Ошибка: сообщение не может быть пустым!") 