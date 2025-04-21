class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tl = [i for i in t]
        for i in s:
            tl.remove(i)
        return tl[0]
