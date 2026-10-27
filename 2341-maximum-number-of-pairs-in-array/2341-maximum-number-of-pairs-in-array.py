class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        pairs=0
        leftover=0
        for i in set(nums):
            count=nums.count(i)
            pairs+=count//2
            leftover+=count%2
        return pairs,leftover


        
