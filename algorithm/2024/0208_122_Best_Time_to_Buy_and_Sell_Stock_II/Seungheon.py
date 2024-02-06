class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 최대 이득을 갱신하는 방식
      
        benefit = 0
        for i, p_i in enumerate(prices):
            if i == 0:
                continue
            benefit = max(benefit, benefit + p_i -prices[i-1])
          
        return benefit
