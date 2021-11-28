# dp로 품
# substring을 만들어 품
# S[:i]를 이용해 t[:j]를 만들 수 있는 경우의 수를 구함
# 만약 이 상황에서 t[j:] 안에 s[i]와 같은 것이 있으면 그 개수만큼 +1을 해주는 식으로 품

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0 for i in range(len(t)+1)]
        dp[0] = 1 # 우선 s[:0]과 t[:0]은 같다고 둠
        
        for i in range(len(s)):
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    dp[j+1] = dp[j] + dp[j+1]
        
        return dp[-1]
