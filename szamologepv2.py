import unittest

def szamologep(elsoszam, masodikszam, muvelet):
    if muvelet not in ["+", "-", "*", "/"]:
        return "Hibás művelet!"
    if muvelet == "+":
        eredmeny = elsoszam + masodikszam
    elif muvelet == "-":
        eredmeny = elsoszam - masodikszam
    elif muvelet == "*":
        eredmeny = elsoszam * masodikszam
    elif muvelet == "/":
        if not masodikszam == 0:
            eredmeny = elsoszam / masodikszam
        else:
            return "Nullával nem osztunk!"
    return eredmeny

class TestSzamologep(unittest.TestCase):
    def testOsszeadas(self):
        self.assertEqual(szamologep(2, 3, "+"), 5)

    def testKivonas(self):
        self.assertEqual(szamologep(5, 2, "-"), 3)

    def testSzorzas(self):
        self.assertEqual(szamologep(3, 4, "*"), 12)

    def testOsztas(self):
        self.assertEqual(szamologep(10, 2, "/"), 5)

    def testHibasMuvelet(self):
        self.assertEqual(szamologep(10, 2, "%"), "Hibás művelet!")

    def testNullavalOsztas(self):
        self.assertEqual(szamologep(10, 0, "/"), "Nullával nem osztunk!")

unittest.main()