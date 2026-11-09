class Solution:
    def findGCD(self, nums: list[int]) -> int:
        greatest=0
        for i in nums:
            if i>greatest:
                greatest=i
        smallest=greatest
        for i in nums:
            if i<smallest:
                smallest=i
        a=greatest
        b=smallest
        c=[]
        d=[]
        for i in range(1,a+1):
            if a%i==0:
                c.append(i)
        for j in range(1,b+1):
            if b%j==0:
                d.append(j)
        maximun=0
        for i in d:
            if i in c:
                if i>maximun:
                    maximun=i
        return maximun