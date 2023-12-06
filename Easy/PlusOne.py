class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        niz = ''
        for el in digits:
            niz += str(el)
        cifra = int(niz)
        cifra += 1
        tab = []
        for st in str(cifra):
            tab.append(int(st))
        return tab