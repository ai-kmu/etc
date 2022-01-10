class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dynamic programming 방식으로 문제 풀이
        
        dp = [0] * (days[-1]+1) # dp배열의 길이: 마지막으로 여행해야 하는 날짜 + 1

        for i,v in enumerate(dp):
            # dp배열의 0번째 인덱스는 0으로 시작
            if i == 0:
                dp[i] = 0
            
            # i가 days에서 여행해야 하는 날이면 경비 계산
            # 여행해야 하는 날은 아래 3개 값 중 최소값을 선택
            # dp[i-1]+cost[0], dp[i-7]+cost[1], dp[i-30]+cost[2]
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
            
            # 여행 안하는 날에는 이전 인덱스에서의 dp값 저장
            else:
                dp[i] = dp[i-1]
        return dp[-1] # 최종 답은 dp의 마지막 인덱스에서의 dp값을 출력
        
