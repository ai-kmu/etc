class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 앞뒤 차이가 0 이상일때를 더하면 됨
        return sum([b - a for a, b in zip(prices[:-1], prices[1:]) if b > a])                
