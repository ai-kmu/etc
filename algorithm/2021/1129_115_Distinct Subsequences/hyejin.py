class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)
        
        dp = [0]*m 
        
        # 각 index에 연속되는 substring 저장
        for i in range(n):
            prev = 1
            for j in range(m):
                if s[i] == t[j]: # character 같으면
                    # prev는 dp[j]로, dp[j]은 바뀌기 전의 prev+dp[j]
                    prev,dp[j] = dp[j],prev+dp[j]
                else: # 같지 않으면, 그대로
                    prev = dp[j]
                    
        return dp[m-1]
