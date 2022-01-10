class Solution: 
    def mincostTickets(self, days, costs):
        # 문제: 여행비용이 최소가 되도록 여행 티켓 1,7,30 골라서 사기
        dp = [0] * (days[-1] + 1) # 날짜보다 하루 많은 dp 배열 생성

        for i in range(1, len(dp)):
            if i not in days: # 여행 안 한 날
                dp[i] = dp[i - 1] # 그 전 날과 여행 소모비용 동일하고 최소값 유지

            else: # 여행 한 날
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0 , i-30)] + costs[2])
                # 1일권 구매, 7일권 구매, 30일권 구매 각각의 경우에서 최소 비용 채택
                # 1일권 구매는 동일하게 비용이 추가.
                # 7일권, 30일권 구매는 1일권 여러 번 구매보다 싼 경우가 있기때문에 최소값을 따진다.

        return dp[-1]
