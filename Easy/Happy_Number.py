class Solution:
    def isHappy(self, n: int) -> bool:
        ze_izracunani = set()
        rez = 0

        while n != 1:
            if n in ze_izracunani:
                return False
            for st in str(n):
                rez += int(st)**2
            n = rez
        return True