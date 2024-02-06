class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        num = len(prices)
        profit = 0
        
        # 비싸지면 팔고 차액만큼 수익 추가
        for i in range(1, num):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit
