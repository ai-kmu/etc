class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = ''
        
        ss = sum(ord(x) for x in s)
        tt = sum(ord(y) for y in t)

        ans = chr(tt-ss)

        return ans
