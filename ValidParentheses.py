class Solution:
    def isValid(self, string: str) -> bool:
        stevec_preklepajev = 0
        stevec_zaklepajev = 0 
        sklad = []
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
                sklad.append(okl)

            elif okl in ")]}":      # ce je znak zaklepaj, iz sklada vzamemo zadnji element
                stevec_zaklepajev += 1
                if len(sklad) < 1:
                    return False    # ce je sklad prazen (in smo nasli zaklepaj), vrnemo False
                vrhnji = sklad[-1]    
                if vrhnji == sl[okl]:
                    sklad.pop()
                else:
                    return False  # ce vrhnji element sklada ni enak ustreznemu zaklepaju, vrnemo False

        if stevec_preklepajev == stevec_zaklepajev and len(sklad) == 0:  # ce je sklad prazen, in ce je predklepajev enako veliko kot zaklepajev
            return True
        else:
            return False

 