from encoder.modulate import Modulate
from decoder.demodulate import Demodulate

m = Modulate()
d = Demodulate()

t_case_unpacked = {
    "0110": [(-1 + 0j), (0 - 1j)],
    "0011": [(0 + 1j), (1 + 0j)]
}

t_case_packed = {
    "10100110": [(0 - 1j), (0 - 1j), (-1 + 0j), (0 - 1j)],
    "10100011": [(0 - 1j), (0 - 1j), (0 + 1j), (1 + 0j)]
}


def test_modulate():
    for k, v in t_case_unpacked.items():
        assert m.modulate_qpsk(k) == v

# проверяет несоответствие


def test_demodulate_unpacked():
    for k, v in t_case_unpacked.items():
        assert d.demodulate_qpsk(v) != k

# проверяет соответствие


def test_demodulate_packed():
    for k, v in t_case_packed.items():
        assert d.demodulate_qpsk(v) == k
