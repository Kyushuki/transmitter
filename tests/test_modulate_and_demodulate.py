from encoder.modulate import QPSKModulate
from decoder.demodulate import Demodulate

m = QPSKModulate()
d = Demodulate()

def test_modulate():
   t = [
      "11001111111100001110100011100010111001011111001000100001",
      "01100001011000100110001101100100",
      "101101101010",
      "000100000010000000"
   ]
   for i in t:
    assert d.demodulate(m.modulate(i)) == i