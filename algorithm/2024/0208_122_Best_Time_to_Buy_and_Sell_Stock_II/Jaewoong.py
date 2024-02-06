class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 쌀 때 사고 비쌀 때 팔고
        # 결과 값 할당
        result = 0

        for i in range(len(prices) - 1):
            # 결국 이후 값이 이전 값보다 크면 되는 듯...
            if prices[i + 1] > prices[i]:
                result += prices[i+1] - prices[i]            
            pass

        return result
