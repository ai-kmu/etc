# fail code

from collections import deque
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mono_Q = [prices[0]] # 0, 1, 2, 3, 4
        prv_Q_money = 0
        
        dp = [0 for _ in prices]

        for p_i, p in enumerate(prices):

            # 최솟값보다 작은거나 같은것 들어오면
            if mono_Q[0] >= p:
                if p_i >= 2:
                    prv_Q_money = dp[p_i-2]
                else:
                    prv_Q_money = 0

                mono_Q = [p]
            else:
                # 들어온값이 최댓값보다 작으면
                if p < mono_Q[-1]:
                    while p < mono_Q[-1]:
                        mono_Q.pop()
                elif p > mono_Q[-1]:
                    mono_Q.append(p)

            # 값 변경
            Q_money = mono_Q[-1] - mono_Q[0]

            # 지금 큐의 최댓값 - p  + 두개전 큐의 최댓값 , 이전 큐의 최댓값 + 1개 전의 큐의 최댓 차이값 , 
            # print("1",dp[p_i-3] + cur_money, dp[p_i-1])

            if p_i >= 2:
                dp[p_i] = max(dp[p_i-3] + prices[p_i] - prices[p_i-1], dp[p_i-1], dp[p_i-2], dp[p_i-3], Q_money + prv_Q_money)
            else:
                dp[p_i] = Q_money

        return dp[-1]

