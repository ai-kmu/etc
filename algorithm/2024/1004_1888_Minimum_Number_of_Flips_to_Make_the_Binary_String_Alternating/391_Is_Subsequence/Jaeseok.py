class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = len(s)
        i = 0
        if len(s) == 0:
            return True
        for l in t:
            if s[i] == l:
                i += 1
            if i == len(s):
                return True
        else:
            return False
          
