class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        unique = []

        for i in nums:
            if i not in unique and i != 0:
                unique.append(i)

        return len(unique)