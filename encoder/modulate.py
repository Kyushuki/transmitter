class Modulate():
    """
    Класс модуляции QPSK
    """
    map = {
        "00": complex(0, 1),
        "01": complex(-1, 0),
        "10": complex(0, -1),
        "11": complex(1, 0),
    }

    def modulate_qpsk(self, mess: str) -> list[complex]:
        """
        Метод модулирует битовое сообщение в комплексные числа для передачи сигнала

        Параметры:

        mess: string

        Возвращает - list[complex] список комплексных чисел
        """
        res = []
        for i in range(0, len(mess), 2):
            res.append(self.map[mess[i:i + 2]])
        return res
