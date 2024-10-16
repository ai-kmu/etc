class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_range = range(days[-1] + 1)
        dp = [0 for _ in days_range]  # dp table 초기화
        days = set(days)
        
        # days 순회 하면서
        for i in days_range:
            # days에 포함 안 되어 있으면 이전 값 그대로 갖고 옴
            if i not in days:
                dp[i] = dp[i - 1]
            # dp : 세 가지 탑승권을 새로 사는 것 중에 제일 싼 걸로 채워 넣기
            # max는 음수 index를 방지하기 위함
            else:
                one_day = dp[max(0, i - 1)] + costs[0]
                weekly = dp[max(0, i - 7)] + costs[1]
                monthly = dp[max(0, i - 30)] + costs[2]
                dp[i] = min(one_day, weekly, monthly)
        
        return dp[-1]
