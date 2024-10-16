# 1일 ~ days[-1]까지의 dp 테이블 생성 후 매일 최솟값 업데이트

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1]+1)

        for i in range(1, days[-1] + 1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                day1 = dp[i-1] + costs[0]
                
                if i >= 7:
                    day7 = dp[i-7] + costs[1]
                else:
                    day7 = costs[1]
                    
                if i >= 30:
                    day30 = dp[i-30] + costs[2]
                else:
                    day30 = costs[2]
                    
                dp[i] = min(day1, day7, day30)
                
        return dp[-1]
