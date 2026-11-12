class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        seen_chars = set()
        for i in range(len(s)):
            if s[i] in seen_chars:
                continue
                
            alphabet_index = ord(s[i]) - ord('a')
            required_distance = distance[alphabet_index]
            
            if i + required_distance + 1 >= len(s):
                return False
                
            if s[i + required_distance + 1] != s[i]:
                return False
                
            seen_chars.add(s[i])
            
        return True