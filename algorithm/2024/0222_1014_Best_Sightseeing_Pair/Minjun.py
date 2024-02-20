# 분노의 솔루션

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0] * len(values)
        tmp = [v - i+1 for i, v in enumerate(values)]
        # dp[0] = 0
        # dp[1] = v[1] + v[0] + 0 - 1
        # dp[2] = v[2] + v[1] + 1 - 2 or v[2] + v[0] + 0 - 2 or v[1] + v[0] + 0 - 1
        # dp[3] = v[3] + v[2] + 2 - 3 or v[3] + v[1] + 1 - 3 or v[3] + v[0] + 0 - 2 or v[2] + v[1] + 1 - 2 or v[2] + v[0] + 0 - 2 or v[1] + v[0] + 0 - 1
        # dp[4] = v[4] + v[3] + 3 - 4 or v[4] + v[2] + 2 - 4 or ----- or dp[3]
        m = 0
        for i, v in enumerate(values):
            if i == 0:
                continue
            dp[i] = max(values[i-1] + i - 1 , dp[i-1])
            m = max(m, dp[i] + v - i)
        return m
