class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        length = len(s)
        
        dp = [True] + [False] * length      # dp 초기화
        for i in p:                         # p string 패턴 검사 시작
            if i != '*':                    # * 아닌 경우
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:                           # *인 경우
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'     
        return dp[-1]
        
