class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        kupi = prices[0]
        dobicek = 0

        for cena in prices[1:]:
            if kupi < cena: # profitabilna varjanta
                dobicek = max(dobicek, cena - kupi) # preverimo, ali smo prej ze nasli vecji dobicek
            else: # cena je manjsa od kupi
                kupi = cena # dobicek bo zagotovo vecji, ce izberemo manjso od obeh cen za nakup
                
        return dobicek



        