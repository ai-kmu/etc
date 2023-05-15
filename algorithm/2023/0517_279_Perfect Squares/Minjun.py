# 정답 봤씁니다.

import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # 주어진 수에 가능한 최대 제곱수까지 구한다
        sq = int(math.sqrt(n)) + 1
        sq_num = [0] * sq
        for i in range(1, sq):
            sq_num[i] = i * i

        for i in range(1, n + 1):
            for j in range(1, sq):
                if i < sq_num[j]:
                    break
                dp[i] = min(dp[i], dp[i - sq_num[j]] + 1)

        return dp[n]
