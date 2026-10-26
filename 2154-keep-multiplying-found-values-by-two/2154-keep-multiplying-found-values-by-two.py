class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        n=len(nums)
        while n>0:
            if original in nums:
                    original=original*2
            else:
                    break
            
        return original
            