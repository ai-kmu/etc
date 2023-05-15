class Solution:
    def numSquares(self, n: int) -> int:
        dp = [1e10 for _ in range(n+1)]
        dp[0] = 0 # 인덱스 0에 해당되는 dp값은 0으로 초기화. 나머지는 매우 큰 수로 초기화

        # dp[i]: i를 만들기 위한 perfect square number들의 합의 최소 길이
        # j*j가 i보다 작거나 같을 때까지 dp[i-j*j] + 1(j*j로 더했을 때 최소 개수)를 계산한다.
        # dp[i-j*j] + 1을 j를 순회하면서 갱신하여 dp[i]를 계산
        for i in range(1, n+1):
            for j in range(0, int(math.sqrt(i))+1):
                dp[i] = min(dp[i], dp[i-j*j] + 1)
        return dp[n]
