# 팔고 나서 다시 사는 게 가능하다면 (조건에는 명시되어있지 않지만)
# 내일 보다 쌀 때 무조건 미리 샀다가 파는 게 맞음
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        answer = 0
        for i, p in enumerate(prices, 1):
            # 인덱스 초과 방지
            if i == n:
                break
            # 내일보다 오늘이 싸면 사고 팔기
            if p < prices[i]:
                answer += prices[i] - p

        return answer
