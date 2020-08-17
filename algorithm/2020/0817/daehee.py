class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # 홀수 string
            tmp = self.maxPal(s, i, i)
            if len(tmp) > len(res):
                res = tmp
                
            # 짝수 string
            tmp = self.maxPal(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # i번째 문자를 중앙으로 하고, 펠린드럼 max값 까지 구하기
    def maxPal(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return s[left+1:right]
