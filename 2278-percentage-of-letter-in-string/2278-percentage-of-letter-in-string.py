class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n=len(s)
        count=0
        for i in s:
            if i==letter:
                count+=1
        percentage=(count/n)*100
        return int(percentage)