class Demodulate():
    """
    Класс демодуляции QPSK комплексных чисел в биты
    """
    map = {
        "00": complex(0,1),
        "01": complex(-1,0),
        "10": complex(0,-1),
        "11": complex(1,0),
    }

    def demodulate(self,mess: list[complex])-> str:
        """
        Метод превращает комплексные числа в строку битов

        Параметры:

        mess: list[complex] список комплексных чисел

        Возвращает - string
        """
        res=[]
        for i in mess:
            for key, value in self.map.items():
                if i == value:
                    res+=key
        return ''.join(res)
    