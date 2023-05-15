class Solution:
    def numSquares(self, n: int) -> int:
        # 최대 제곱수를 구합니다.
        max_sqrt = int(n ** 0.5)
        # dp 리스트 초기화
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # 1부터 n까지 반복
        for i in range(1, n+1):
            # i보다 작거나 같은 제곱수들 중에서 가장 큰 수를 구합니다.
            for j in range(1, max_sqrt+1):
                if i - j*j < 0:
                    break
                dp[i] = min(dp[i], dp[i-j*j]+1)
        
        return dp[n]
