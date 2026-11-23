class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        even_counts = {}
        for i in nums:
            if i % 2 == 0:
                even_counts[i] = even_counts.get(i, 0) + 1
        if even_counts:
            highest_count = max(even_counts.values())
            result = float('inf')
            for key, value in even_counts.items():
                if value == highest_count:
                    result = min(result, key)
            return result
        else:
            return -1
        