class Solution:
    def romanToInt(self, s: str) -> int:
        slovar = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        rezultat = 0
        naslednja_preverjena = False
        for i, crka in enumerate(s):
            if i + 1 < len(s): # ce obstaja se naslednja crka
            
                if naslednja_preverjena:   # ce imamo situacijo recimo MCM, preverimo M, potem pa CM. Nocemo se enkrat zadnjega M-ja
                    naslednja_preverjena = not naslednja_preverjena
                    continue

                else:
                    if s[i:i+2] in slovar: #ce je naslednja crka v slovarju
                        if slovar[s[i:i+2]] >= slovar[crka]: # in ce je vecja od predhodnje
                            rezultat += slovar[s[i:i+2]] # dodamo sedanjo in naslednjo cifro v rezultat (i+2 pomeni do ukljucno i+1)
                            naslednja_preverjena =  not naslednja_preverjena
                    else:  # ce je sedanja crka vecja od naslednje, jo dodamo v rezultat
                        rezultat += slovar[crka]

        if not naslednja_preverjena: # zadnje crke se nismo preverili
            rezultat += slovar[crka] # jo pristejemo k rezultatu
        return rezultat


