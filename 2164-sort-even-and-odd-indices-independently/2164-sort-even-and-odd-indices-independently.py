class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        even=[]
        odd=[]
        n=len(nums)
        for i in range(n):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort(reverse=True) 
        odd.sort()
        for i in range(n):
            if i % 2 == 0:
                nums[i] = even.pop()
            else:
                nums[i] = odd.pop()
        return nums

        