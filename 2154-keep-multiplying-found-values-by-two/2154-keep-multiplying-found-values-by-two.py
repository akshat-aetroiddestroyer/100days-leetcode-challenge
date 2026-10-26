class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        while True:
            found=False
            for i in nums:
                if original==i:
                    original=original*2
                    found=True
                    break
            if found==False:
                break
        return original
            