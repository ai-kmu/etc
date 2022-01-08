class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day = days[-1] 
        dp = [0] * (day+1) #날짜 배열에 들어있는 마지막 날 + 1 크기의 배열을 생성(모든 값은 0)
        
        
        #1일부터 마지막날까지 돌면서 여행 날짜 배열에 있는 날짜가 아닌 경우에는 바로 전날의 값을 그대로 갖게 하고
        #여행 날짜에 해당하는 날에는 3가지 경우 중에서 가질 수 있는 최소값을 저장한다
        #예를 들어 [1,4,6,7,8,20] 여행 날짜 배열로 보면 1일에 2, 2일에 4, 6일에 6을 갖다가 7일에 8대신에 최솟값인 7을 갖게된다.
        #여기서 max 함수가 쓰인 이유는 7일 , 30일 보다 작은 날을 고려했기 때문이다.
        #즉 7일 이전에 7일권을 사거나 30일 이전에 30일권을 사야하는 경우를 고려하였다.
        for i in range(1 , day + 1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1] + costs[0],dp[max(0,i-7)] + costs[1], dp[max(0,i-30)]+costs[2])
        return dp[day]
