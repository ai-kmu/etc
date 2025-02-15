# 풀이 실패 ㅡㅡ

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ds, dt = defaultdict(int), defaultdict(int)
        for i in s:
            ds[i] += 1
        for i in t:
            dt[i] += 1
        for i in dt.keys():
            if ds[i] < dt[i]:
                return ""
        left, right = 0,0
        now = []
        tmp = 10**5+1
        for idx, c in enumerate(s):
            if c in dt.keys():
                dt[c] -= 1
                if max(dt.values()) > 0:
                    if dt[c] >= 0:
                        now.append(idx)
                        right = idx
                    else:
                        now.append(idx)
                        left = min(now)
                elif max(dt.values()) == 0:
                    right = idx
                    left = min(now)
                    if tmp > right - left:
                        tmp = right - left
                        ans = s[left:right+1]
                else:
                    min(now)
                    now.pop(min(now))
                    now.append(idx)
        return ans
