class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        flag = [False] * len(s)

        for iii, i in enumerate(s):
            for ii in range(idx, len(t)):
                if i == t[ii]:
                    idx += 1
                    flag[iii] = True
                    break
                else:
                    idx += 1
                    continue

        if sum(flag) == len(s):
            return True
        else:
            return False
