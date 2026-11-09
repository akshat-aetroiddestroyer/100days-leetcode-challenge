class Solution:
    def findGCD(self, nums: list[int]) -> int:
        maxi=max(nums)
        mini=min(nums)
        a=[]
        b=[]
        for i in range(1,maxi+1):
            if maxi%i==0:
                a.append(i)
        for j in range(1,mini+1):
            if mini%j==0:
                b.append(j)
        maximum=0
        for i in a:
            if i in b:
                if i>maximum:
                    maximum=i
        return maximum