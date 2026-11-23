class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        visited=[]
        for i in nums:
            if i not in visited and i!=0:
                visited.append(i)
        return len(visited)