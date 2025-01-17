class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 예외케이스
        if n == 1:
            return 0
        
        # DP 할당
        # last_*는 현재 (마지막) 액션이 *
        last_buy = [-10 ** 10 for _ in range(n)]
        last_sell = [0 for _ in range(n)]
        for i, p in enumerate(prices):
            # 현 시점에 팔려면
            last_sell[i] = max(
                last_sell[i - 1],    # i-1: 팔고 / i: 가만히
                last_buy[i - 1] + p  # i-1: 사고 / i: 팔기
            )                        # 둘 중에 최댓값으로 넣기 (DP)
            # 현 시점에 사려면
            last_buy[i] = max(
                last_buy[i - 1],        # i-1: 사고 / i: 가만히
                # last_buy[i - 1] - p,  # i-1: 사고 / i: 또 사기  <- max가 될리 없음
                last_sell[i - 2] - p    # i-2: 팔고 / i: 사기 (i-1 쿨다운)
            )                           # 셋 중에 최댓값으로 넣기 (DP)

        return last_sell[-1]
