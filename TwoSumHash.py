class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            '''Vrne indeksa elementov v tabeli nums, kjer je vsota
            elementov enaka stevilu target'''
            hashMap = {}
            n = len(nums)

            # zgradimo hashmap
            for i in range(n):
                hashMap[nums[i]] = i
            
            # preverimo ali lahko najdemo par
            for i in range(n):
                razlika = target - nums[i]
                if razlika in hashMap and hashMap[razlika] != i: # ne smemo sesteti enakega elementa dvakrat (el na istem mestu)
                    return i, hashMap[razlika]