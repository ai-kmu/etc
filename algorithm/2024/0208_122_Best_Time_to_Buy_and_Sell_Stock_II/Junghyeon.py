# DP로 풀이
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        result = 0

        for i in range(1, len(prices)):
            # 이전 가격보다 클 경우 둘의 차이가 이익이 됨
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]
        
        return result
