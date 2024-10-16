class Solution:
    def mincostTickets(self, days, costs):
        last_day = days[-1]
        travel_days = days 
        dp = [0] * (last_day + 1)
        for day in range(1, last_day + 1):
            dp[day] = dp[day - 1]
            if day in travel_days:
                dp[day] = min(
                    costs[0] + dp[max(0, day - 1)],
                    costs[1] + dp[max(0, day - 7)],
                    costs[2] + dp[max(0, day - 30)])
        return dp[-1]
