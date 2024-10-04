class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cnt = 0
        for si in range(len(s)):
            for ti in range(len(t)):
                if s[si] == t[ti]:
                    t = t[ti+1:]
                    cnt = cnt + 1
                    break
                if ti == len(t)-1:
                    break
        return cnt == len(s)
