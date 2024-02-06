class Solution(object):
    def maxProfit(self, prices):
        asw = 0
        for i in range(1, len(prices)):
            # 이전 값보더 더 크면 차익만큼 추가
            if prices[i] > prices[i - 1]:
                asw += prices[i] - prices[i - 1]
        return asw
