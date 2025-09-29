class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        ans = ""
        for idx, t in enumerate(a):
            b = t[::-1]
            if idx != len(a)-1:
                b += " "
            ans += b
        return ans
