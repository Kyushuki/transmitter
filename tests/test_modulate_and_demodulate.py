from encoder.modulate import Modulate
from decoder.demodulate import Demodulate

m = Modulate()
d = Demodulate()

t = {
    "0110": [(-1 + 0j), (0 - 1j)],
    "0011": [(0 + 1j), (1 + 0j)]
}


def test_modulate():
    for k, v in t.items():
        assert m.modulate_qpsk(k) == v


def test_demodulate():
    for k, v in t.items():
        assert d.demodulate_qpsk(v) == k
