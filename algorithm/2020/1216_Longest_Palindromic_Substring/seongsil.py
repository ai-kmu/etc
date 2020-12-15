class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                if(s[j:j+i] == s[j:j+i][::-1]):
                    return s[j:j+i]
