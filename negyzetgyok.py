import unittest
import math

def negyzetgyok(x):
    if x > 0:
        return math.sqrt(x)
    else:
        return "Negativ szambol nem vonunk negyzetgyokot!"

class TestNegyzetgyok(unittest.TestCase):
    def testPozitiv(self):
        self.assertGreater(negyzetgyok(1.4), 0)

    def testNegativ(self):
        self.assertEqual(negyzetgyok(-234324), "Negativ szambol nem vonunk negyzetgyokot!")

    def testNulla(self):
        self.assertEqual(negyzetgyok(0), "Negativ szambol nem vonunk negyzetgyokot!")

unittest.main()