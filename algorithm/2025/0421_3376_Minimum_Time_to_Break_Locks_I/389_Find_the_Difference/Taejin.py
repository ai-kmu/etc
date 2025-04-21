from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return "".join([c for c in set(t) if t.count(c) != s.count(c)])
