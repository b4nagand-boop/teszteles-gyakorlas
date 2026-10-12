import unittest

def hibas_abs(x):
    return -x

def jo_abs(x):
    if x < 0:
        return -x
    else:
        return x

fgv = jo_abs
class TestHibasAbs(unittest.TestCase):
    def test_positive(self):
        self.assertGreater(fgv(5), 0)

    def test_negative(self):
        self.assertEqual(fgv(-3), 3)

    def test_zero(self):
        self.assertEqual(fgv(0), 0)

unittest.main()