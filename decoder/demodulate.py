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
        beta = np.abs(z / z0)
        # print(beta)
        phi = a - b
        # print(mess)
        if abs(phi) >= 1e-6:
            r = complex(np.exp(-1j * phi))
            mess = [c * r for c in mess]
            # print(phi)
        mess = [c / beta for c in mess]
        res = []
        print(f"Так выглядит перед модуляцией: \n{mess}")
        for i in mess:
            min_dist = float('inf')
            k = ""
            for key, value in self.map.items():
                if abs(i - value) < min_dist:
                    min_dist = abs(i - value)
                    k = key
            res += k
        print(''.join(res))
        return ''.join(res)
