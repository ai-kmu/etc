class Solution:
    def numSquares(self, n: int) -> int:
        # dp를 활용한 풀이
        dp = [-1] * (n + 1)
        
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n+1):
            # 자신보다 작은 제곱수들을 뺀 위치의 dp table 값을 가져와서 1을 더해서 최솟값을 구함
            tmp = float('inf')
            for j in range(1, int(i ** 0.5)+1):
                tmp = min(dp[i - j * j] + 1, tmp)
            dp[i] = tmp

        return dp[-1]
