class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_val = 0
        for i in range(len(s)):
            sum_val ^= ord(s[i])
        for i in range(len(t)):
            sum_val ^= ord(t[i])
        
        return chr(sum_val)
