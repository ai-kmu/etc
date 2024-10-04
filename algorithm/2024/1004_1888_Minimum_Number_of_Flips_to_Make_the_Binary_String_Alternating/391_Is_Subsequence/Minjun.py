class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        flag = True
        if len(s) > len(t):
            return False
        if len(s) == len(t) and s != t:
            return False
        while flag and i < len(s):
            c = s[i]
            if c in t:
                k = t.index(c)

                t = t[k+1:]
            else:
                flag = False
            i += 1
        return flag
