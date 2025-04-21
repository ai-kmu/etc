from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        for k, v in t.items():
            if v != s[k]: return k
