class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        freq={}
        ans=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num,count in freq.items():
                if count==2:
                    ans.append(num)
                    break
        n=len(nums)
        for i in range(1,n+1):
            if freq.get(i,0)==0:
                ans.append(i)
        return ans
