class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a = s.split()
        d1 = {}
        d2 = {}
        if len(pattern) != len(a):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d1:
                # Check whether existing mapping matches a[i]
                if d1[pattern[i]] != a[i]:
                    return False
                    break
            else:
                d1[pattern[i]] = a[i]
            if a[i] in d2:
                # Check reverse mapping
                if d2[a[i]] != pattern[i]:
                    return False
                    break
            else:
                d2[a[i]] = pattern[i]
        else:
            return True