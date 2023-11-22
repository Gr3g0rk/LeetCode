class Solution:
    def isValid(self, string: str) -> bool:
        stevec_preklepajev = 0
        stevec_zaklepajev = 0 
        sklad = Sklad()
        sl = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # ce imamo prazen niz ali samo en oklepaj
        if len(string) <= 1:
            return False

        # pregledamo vse znake v nizu
        for okl in string:
            if okl in "([{":    # ce je znak predklepaj, ga dodamo na sklad in povecamo stevec predklepajev
                stevec_preklepajev += 1
                sklad.vstavi(okl)

            elif okl in ")]}":      # ce je znak zaklepaj, iz sklada vzamemo zadnji element
                stevec_zaklepajev += 1
                try:
                    vrhnji = sklad.vrh()    # ce je sklad prazen, bomo dobili error -> vrnemo False
                except ValueError:
                    return False

                if vrhnji == sl[okl]:
                    sklad.odstrani()
                else:
                    return False  # ce vrhnji element sklada ni enak ustreznemu zaklepaju, vrnemo False

        if stevec_preklepajev == stevec_zaklepajev and sklad.prazen():  # ce je sklad prazen, in ce je predklepajev enako veliko kot zaklepajev
            return True
        else:
            return False


# IMPLEMENTACIJA SKLADA

class Sklad:
    def __init__(self):
        self.podatki = []

    def vstavi(self, x):
        self.podatki.append(x)

    def prazen(self):
        return len(self.podatki) == 0

    def odstrani(self):
        if self.prazen(): raise ValueError('ODSTRANI: Sklad je prazen.')
        self.podatki.pop()

    def vrh(self):
        if self.prazen(): raise ValueError('VRH: Sklad je prazen.')
        return self.podatki[-1]

    def __str__(self):
        izp = 'DNO'
        for elt in self.podatki: izp += ' : ' + str(elt)
        return izp + ' : VRH'