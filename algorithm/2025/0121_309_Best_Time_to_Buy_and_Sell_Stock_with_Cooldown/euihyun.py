# 리뷰 x 안풀렸음 바로 아래는 실패 코드, 정답보고 수정함.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 사고 - 팔고 - 기다리고 
        # 전체를 보고 결정가능 = 제일 득이 큰 날을 찾을수 있다는뜻, 근데 기다리는걸 생각해야됨
        n = len(prices)
        dp = [0 for _ in range(n)]
        max_table = []
        
            
        if n == 1:
            return 0
        if n == 2 and prices[0] < prices[1]:
            return prices[1] - prices[0]
        
        for i in range(n-2):
            if prices[i] <= prices[i+1] and prices[i+1] < prices[i+2]:
                dp[i] = prices[i] - prices[i+2]
            else:
                dp[i] = min(prices[i] - prices[i+1], prices[i+1] - prices[i+2])
        print(dp)
        for j in range(n-1):
            if dp[j] >= 1:
                dp[j] = 0
            if dp[j] == dp[j+1]:

                dp[j+1] = 0
        
        return (sum(dp))*(-1)
            

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0

        # DP 배열 초기화
        hold = [-float('inf')] * n
        cash = [0] * n
        cooldown = [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            # 존버의 최대이익
            hold[i] = max(hold[i - 1], cash[i - 1] - prices[i])
            # 자유로운 영혼의 최대값
            cash[i] = max(cash[i - 1], cooldown[i - 1])
            # 쿨다운 포함한 최대값
            cooldown[i] = hold[i - 1] + prices[i]

        # 최종 상태 중 cash와 cooldown 중 최댓값 반환
        return max(cash[-1], cooldown[-1])
        
