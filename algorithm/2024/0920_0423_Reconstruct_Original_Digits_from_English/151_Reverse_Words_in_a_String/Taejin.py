class Solution:
    def reverseWords(self, s: str) -> str:
        ret = s.strip()
        ret = ret.split()[::-1]
        return " ".join(ret)
        
