from math import inf
from typing import List

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        n = len(strength)
        # 자물쇠가 하나만 있을 때도 coef=1이므로 strength[0] // 1, ceil 처리 후 리턴
        if n == 1:
            return strength[0]

        totalStates = 1 << n
        INF = inf
        dp = [INF] * totalStates
        dp[0] = 0

        for mask in range(totalStates):
            cnt = mask.bit_count()           # 깬 자물쇠 개수
            coef = 1 + cnt * k               # 현재 에너지 증가 계수

            for i in range(n):
                if not (mask & (1 << i)):
                    # ceil(strength[i] / coef)
                    t = (strength[i] + coef - 1) // coef
                    nxt = mask | (1 << i)
                    dp[nxt] = min(dp[nxt], dp[mask] + t)

        return dp[-1]
