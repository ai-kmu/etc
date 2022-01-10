class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 큰 수로 dp를 초기화 합니다
        # dp는 days보다 1더 크게 만듭니다
        dp = [float("inf") for i in range(days[-1]+1)]
        # dp의 첫 번째를 0으로 초기화 합니다.
        dp[0] = 0
        # 몇 번째 날짜인지 구분할 수 있도록 간격을 저장하는 리스트를 만들어줍니다
        count = [1, 7, 30]
        # 1부터 dp를 반복하면서 days에 있는 날짜를 포함해서 첫 날부터 끝까지 루프를 돕니다
        
        # 정민: for문을 이중으로 사용하면 시간효율성 면에서 조금 비효율적일듯 싶습니다.
        for i in range(1, len(dp)):
#             for j in range(len(count)):
#                 #루프를 돌며 만약 해당 날짜가 days에 있는 날짜라면 dp를 업데이트해줍니다.
#                 if i in days:
#                     # 현재 dp의 값과 갱신할 dp의 값 중 더 작은 값으로 갱신합니다.
#                     # 갱신할 dp값은 1일 비용, 7일 비용, 30일 비용 모두 계산합니다.
#                     # max(0, i-count[j])는 현재 dp의 인덱스를 찾기 위한 것이고 costs에서 해당 비용을 더해줍니다.
#                     dp[i] = min(dp[i], dp[max(0,i-count[j])]+costs[j])
#                 else:
#                     # 만약 days와 일치하지 않는 날짜라면 그냥 i-1에 있는 값을 다음 인덱스인 i로 넘겨줍니다.
#                     dp[i] = dp[i-1]
                #루프를 돌며 만약 해당 날짜가 days에 있는 날짜라면 dp를 업데이트해줍니다.
    
        # ---------------------------------제안 코드------------------------------------------
            if i in days:
                # 현재 dp의 값과 갱신할 dp의 값 중 더 작은 값으로 갱신합니다.
                # 갱신할 dp값은 1일 비용, 7일 비용, 30일 비용 모두 계산합니다.
                # max(0, i-count[j])는 현재 dp의 인덱스를 찾기 위한 것이고 costs에서 해당 비용을 더해줍니다.
                dp[i] = min(dp[i], dp[max(0,i-count[0])]+costs[0], dp[max(0,i-count[1])]+costs[1], dp[max(0,i-count[2])]+costs[2])
            else:
                # 만약 days와 일치하지 않는 날짜라면 그냥 i-1에 있는 값을 다음 인덱스인 i로 넘겨줍니다.
                dp[i] = dp[i-1]
        # ------------------------------------------------------------------------------------
        return dp[-1]
