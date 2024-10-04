class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        if len(s) == 0:
            return True
        for i in t:
            if i == s[s_idx]:
                s_idx += 1
                if s_idx == len(s):
                    return True
        return False
