class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        elif len(t) == 0:
            return False
        
        else:
            i, j = 0, 0

            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1

                j += 1

            return i == len(s)
