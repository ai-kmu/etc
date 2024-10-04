class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        s_point  = 0

        for i, t_i in enumerate(t):
            if t_i == s[s_point]:
                s_point += 1

            if s_point >= len(s):
                return True
            

        return False
