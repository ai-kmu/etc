class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # 1 일전 , 7일 전 # 30 일전과 비교
        days_set = set(days)
        # 가격
        dp = [0]*365

        for i in range(len(dp)):

            # 없는 날짜는 이전 날짜 그대로
            day = i + 1
            if day not in days_set:
                if i != 0:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = 0
                continue

            # dp에 현재 가질 수 있는 최솟값 채워가기
            min_cost = float('inf')
            if i >= 1:
                min_cost = min(min_cost, dp[i-1]+costs[0])
            else:
                min_cost = min(min_cost, costs[0])
            if i >= 7:
                min_cost = min(min_cost, dp[i-7]+costs[1])
            else:
                min_cost = min(min_cost, costs[1])
            if i >= 30:
                min_cost = min(min_cost, dp[i-30]+costs[2])
            else:
                min_cost = min(min_cost, costs[2])

            dp[i] = min_cost

        return dp[-1]
