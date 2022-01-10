class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp array 초기화
        dp = [0 for _ in range(days[-1]+1)]
        
        # 1일부터 days의 마지막날까지 탐색
        for day in range(1, days[-1]+1):
            if day in days: #day가 days 안에 들었다면, cost 업데이트
                if day >= 30: # 30일 이상일 때
                    dp[day] = min(dp[day-1]+costs[0], dp[day-7]+costs[1], dp[day-30]+costs[2])
                elif day >= 7: # 7일 이상일 때
                    dp[day] = min(dp[day-1]+costs[0], dp[day-7]+costs[1], costs[2])
                else: # 7일 미만일 때
                    dp[day] = min(dp[day-1]+costs[0], costs[1], costs[2])
                  
#                 다른 간단한 방법
#                 dp[day] = min(costs[0] + dp[max(0, day-1)], costs[1] + dp[max(0, day-7)], costs[2] + dp[max(0, day-30)])
            else: # 아니라면 그냥 day-1의 cost 가져오기
                dp[day] = dp[day-1]
                
        return dp[-1] # 마지막날의 min cost 반환
        
