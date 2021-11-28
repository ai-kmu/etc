class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Dynamic programming 사용
        # 현재 s의 앞의 i개, t의 앞의 j개를 사용했을 때 가능한 경우의 수(=dp[i][j]를 구하고자 한다면
        # 만약 s의 i번째와 t의 j번쨰가 같을 경우
        # 해당 문자를 skip하거나 사용할 수 있음
        # 따라서 skip하는 경우의 수 dp[i-1][j]와 사용하는 경우의 수 dp[i-1][j-1]을 더함
        # 만약 다를 경우
        # 무조건 skip할수 밖에 없음
        # 따라서 dp[i-1][j]를 설정함
        # base case: 
        # 만약 t의 길이가 0일 경우 -> 경우의 수는 1임
        # 만약 s의 길이가 0일 경우 -> t의 길이가 0일때를 제외하고는 경우의 수가 0임
        
        n, m = len(s), len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]
        # base case
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]: 
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else: 
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][m]
