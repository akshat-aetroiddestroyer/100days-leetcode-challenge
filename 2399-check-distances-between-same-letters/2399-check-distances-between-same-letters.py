class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        a = ord('a')
        for i in s:
            idx1 = s.find(i)
            idx2 = s.find(i,idx1+1)
            if distance[ord(i)-a] != idx2 - idx1 - 1:
                return False
        return True