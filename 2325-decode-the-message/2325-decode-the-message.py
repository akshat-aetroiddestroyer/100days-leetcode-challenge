class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        visited = ""
        alpha='abcdefghijklmnopqrstuvwxyz'
        answer=''
        for i in key:
            if i != ' ' and i not in visited:
                visited+=i
        for i in message:
            if i in visited:
                answer+=alpha[visited.index(i)]
            else:
                answer+=i
        return answer
