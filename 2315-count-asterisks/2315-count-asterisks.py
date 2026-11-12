class Solution:
    def countAsterisks(self, s: str) -> int:
        bar_even=True 
        star=0
        for i in s:
            if i == '|':
                bar_even = not bar_even
            elif i == '*' and bar_even:
                star += 1   
        return star