class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        output = []
        for i in range(len(number)):
            if number[i] == digit: #1,2,4
                output.append(number[:i]+number[i+1:]) #number[0:4]+number[4+1:]  = 13235,13235,13325
        return max(output)