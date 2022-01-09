class Solution(object):
    def mincostTickets(self, days, costs):
        ## dp 방식
        
        dp = [0]*366
        ## dp방식으로 각 day에 대한 cost 저장용 리스트
        
        for i in days:
            dp[i] = 1       
        ## days의 날짜만 연산하기 위해 365일 중 days를 1로 나머지를 0로 분류하기
        
        for i in range(1,366):
            if 0 == dp[i]:
                dp[i] = dp[i-1]
            ## days에 없는 날이면 이전 날짜 cost 복붙하기
            
            else:
                ## days에 있는 날이면
                dp[i] = min(costs[0]+dp[i-1], costs[1]+dp[max(0,i-7)], costs[2]+dp[max(0,i-30)])
                ## 전날의 cost에 1일권, 7일권, 30일권을 더한 가격중 가장 작은 값을 cost로 설정
        return dp[-1]
