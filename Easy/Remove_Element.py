class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # imamo stevec ind, ki bo na doloceno mesto v tabeli postavil elemente, ki niso enaki val

        dolzina = len(nums)
        ind = 0

        for el in range(dolzina):
            if nums[el] != val:
                nums[ind] = nums[el]
                ind += 1
        # ne smemo vrniti len(nums), ker so na koncu lahko se elementi
        return ind
        
        
        