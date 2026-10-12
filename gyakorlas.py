import unittest

def gyakorlati_jegy(pontszam: int):
    if pontszam <= 100 and pontszam >= 85:
        erdemjegy = "Jeles (5)"
    elif pontszam <= 84 and pontszam >= 70:
        erdemjegy = "Jó (4)"
    elif pontszam <= 69 and pontszam >= 55:
        erdemjegy = "Közepes (3)"
    elif pontszam <= 54 and pontszam >= 40:
        erdemjegy = "Elégséges (2)"
    elif pontszam <= 39 and pontszam >= 0:
        erdemjegy = "Elégtelen (1)"
    else:
        return("Érvénytelen érték!")
    return(f"Az érdemjegyed > {erdemjegy}")

class TestGyakJegy(unittest.TestCase):
    def testOtosLow(self):
        self.assertEqual(gyakorlati_jegy(85), "Az érdemjegyed > Jeles (5)")

    def testOtosHigh(self):
        self.assertEqual(gyakorlati_jegy(100), "Az érdemjegyed > Jeles (5)")

    #----------------------------------------------------------------------------------------#

    def testNegyesLow(self):
        self.assertEqual(gyakorlati_jegy(70), "Az érdemjegyed > Jó (4)")
        
    def testNegyesHigh(self):
        self.assertEqual(gyakorlati_jegy(84), "Az érdemjegyed > Jó (4)")

    #----------------------------------------------------------------------------------------#

    def testHarmasLow(self):
        self.assertEqual(gyakorlati_jegy(55), "Az érdemjegyed > Közepes (3)")

    def testHarmasHigh(self):
        self.assertEqual(gyakorlati_jegy(69), "Az érdemjegyed > Közepes (3)")

    #----------------------------------------------------------------------------------------#

    def testKettesLow(self):
        self.assertEqual(gyakorlati_jegy(40), "Az érdemjegyed > Elégséges (2)")

    def testKettesHigh(self):
        self.assertEqual(gyakorlati_jegy(54), "Az érdemjegyed > Elégséges (2)")

    #----------------------------------------------------------------------------------------#

    def testEgyesLow(self):
        self.assertEqual(gyakorlati_jegy(0), "Az érdemjegyed > Elégtelen (1)")

    def testEgyesHigh(self):
        self.assertEqual(gyakorlati_jegy(39), "Az érdemjegyed > Elégtelen (1)")

    #----------------------------------------------------------------------------------------#

    def testInvalidLow(self):
        self.assertEqual(gyakorlati_jegy(-1), "Érvénytelen érték!")

    def testInvalidHigh(self):
        self.assertEqual(gyakorlati_jegy(101), "Érvénytelen érték!")

unittest.main()