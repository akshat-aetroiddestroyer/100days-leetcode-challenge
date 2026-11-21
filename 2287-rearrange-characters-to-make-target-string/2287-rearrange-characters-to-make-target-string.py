class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        max=[]
        for i in target:
            max.append(s.count(i)//target.count(i))
        return min(max)