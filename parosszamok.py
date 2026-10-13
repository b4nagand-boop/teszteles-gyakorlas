import unittest

def parosSzamSzum(x: int, y: int):
    osszeg = int()
    for i in range(x, y+1):
        if i%2 == 0:
            osszeg += i

    if y < 0:
        return(None)

    return osszeg

class TestPSzSzum(unittest.TestCase):
    def test1(self):
        self.assertEqual(parosSzamSzum(30, 40), 210)

    def test1esfel(self):
        self.assertGreater(parosSzamSzum(1, 4), 0)

    def test2(self):
        self.assertEqual(parosSzamSzum(0, 0), 0)

    def test3(self):
        self.assertIsNone(parosSzamSzum(9, -16), None)

    def test4(self):
        self.assertIsNone(parosSzamSzum(-22, -9), None)

unittest.main()