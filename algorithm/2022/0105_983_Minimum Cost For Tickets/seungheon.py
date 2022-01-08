class Solution(object):
    def mincostTickets(self, days, costs):
        
        #최대가능한 일수만큼 dp생성
        dp = [0]*365
        #입력받은 날짜가 있으면 count += 1 
        count = 0
        
        # 365일 만큼 for문 반복
        for i in range(len(dp)):
            # 입력받은 날짜와 반복하는 일 수 가 같으면
            if days[count] == i+1 :
                # dp 에 저장된 1 일전의 최소비용 + costs[0]
                # dp 에 저장된 7 일전의 최소비용 + costs[0]
                # dp 에 저장된 30 일전의 최소비용 + costs[0]
                a = dp[i-1] + costs[0]
                b = dp[i-7] + costs[1]
                c = dp[i-30] + costs[2]
                # 셋중 가장 저렴한 비용 선택
                dp[i] = min(a,b,c) 
                # 입력받은 날짜와 비교하기위해 입력받은 날짜를 처리할때마다 count += 1
                count += 1
            # 입력받은 날짜에 없는경우 바로 전날의 날짜와 같은 값을 저장
            else :
                dp[i] = dp[i-1]
            # 입력받은 최대일자에 도달하면 최솟값 반환
            if count == len(days):
                return dp[days[-1]-1]