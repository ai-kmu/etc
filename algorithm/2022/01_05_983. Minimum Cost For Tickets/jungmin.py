class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1]+1)

        for i,v in enumerate(dp):
            if i == 0:
                dp[i] = 0
                
            elif i in days:
                a = costs[2]
                b = costs[1]
                c = costs[0]
                
                if i-30 >= 0:
                    a = dp[i-30] + costs[2]
                if i-7 >= 0:
                    b = dp[i-7] + costs[1]
                if i-1 >= 0:
                    c = dp[i-1] + costs[0]
                    
                dp[i] = min(a,b,c)
                
            else:
                dp[i] = dp[i-1]
        return dp[-1]
        
