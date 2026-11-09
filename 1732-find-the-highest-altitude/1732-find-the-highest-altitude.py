class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        sum=0
        b=[]
        for i in gain:
            sum+=i
            b.append(sum)
        max=0
        for i in b:
            if i>max:
                max=i
        return max