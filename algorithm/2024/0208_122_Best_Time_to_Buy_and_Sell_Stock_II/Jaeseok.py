class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        '''
        주식의 가격이 오르자마자 바로 파는 것이 가장 greedy한 해법
        prices 전체를 순회하면서
        바로 뒤의 가격이 더 비싸다면 answer에 바로 추가
        '''
        for i in range(len(prices) - 1):
            answer += max(0, prices[i + 1] - prices[i])
        return answer
