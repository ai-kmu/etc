class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hand = prices[0]
        profit = 0
        for p in prices:
            # 내가 산 주식보다 가격이 비싸면 걍 팔음
            if p > hand:
                profit = profit + p - hand
                # 팔았으니까 지금 꺼 후보로 둠
                hand = p
            # 후보보다 가격이 싸면 다시 바로 삼
            if p < hand:
                hand = p
        
        return profit
