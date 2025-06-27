import math
import numpy as np


class Demodulate():
    """
    Класс демодуляции QPSK комплексных чисел в биты
    """
    map = {
        "00": complex(0, 1),
        "01": complex(-1, 0),
        "10": complex(0, -1),
        "11": complex(1, 0),
    }

    def demodulate_qpsk(self, mess: list[complex]) -> str:
        """
        Метод превращает комплексные числа в строку битов

        Параметры:

        mess: list[complex] список комплексных чисел

        Возвращает - string
        """
        z0 = complex(0, -1)
        z = mess[0]
        a = math.atan2(z.imag, z.real)
        b = math.atan2(z0.imag, z0.real)
        phi = a - b
        if abs(phi) >= 1e-6:
            r = complex(np.exp(-1j * phi))
            mess = [c * r for c in mess]
        res = []
        for i in mess:
            for key, value in self.map.items():
                if i == value:
                    res += key
        return ''.join(res)
