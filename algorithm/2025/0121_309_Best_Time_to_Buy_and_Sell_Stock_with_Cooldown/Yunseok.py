# 풀이법 참고
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # DP 배열 정의
        dp = [[0] * 3 for _ in range(n)]  # dp[i][0]: i일에 주식 없음, dp[i][1]: i일에 주식 보유, dp[i][2]: i일에 쿨다운 상태

        # 초기 상태 설정
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0

        for i in range(1, n):
            # i일에 주식이 없는 경우: 이전에 주식을 팔거나, 이전에도 주식이 없었음
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])

            # i일에 주식을 보유한 경우: 이전에 주식을 샀거나, 이미 보유 중이었음
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

            # i일에 쿨다운 상태인 경우: 전날 주식을 팔았음
            dp[i][2] = dp[i - 1][1] + prices[i]

        # 마지막 날 최대 이익은 주식을 보유하지 않거나 쿨다운 상태일 때 발생
        return max(dp[n - 1][0], dp[n - 1][2])
        
