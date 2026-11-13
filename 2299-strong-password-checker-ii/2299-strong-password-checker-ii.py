class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        checker=0
        count=0
        if len(password)>=8:                       #8 character min
            checker+=1
        else:
            pass

        count=0
        for i in password:          #check lower char at least 1
            if 'a' <= i <= 'z':
                count+=1
        if count>=1:
            checker+=1
        else:
            pass
        count=0
        for i in password:          #check upper char at least 1
            if 'A' <= i <= 'Z':
                count+=1
        if count>=1:
            checker+=1
        else:
            pass
        count=0
        for i in password:                      #check number present or not
            if '0' <= i <= '9':
                count += 1
        if count >= 1:
            checker+=1
        else:
            pass
        count=0
        "!@#$%^&*()-+"       #special characters atleast 1
        for i in password:
            if i in "!@#$%^&*()-+":
                count += 1
        if count >= 1:
            checker+=1
        else:
            pass
        count=0
        for i in range(len(password)-1):        #adjacent character
            if password[i] == password[i+1]:
                break
        else:
            checker+=1
        if checker>=6:
            return True
        else:
            return False
                