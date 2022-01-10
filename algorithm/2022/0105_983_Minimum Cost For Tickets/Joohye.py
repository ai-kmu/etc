class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:       
        #ex)days=(1,5,6,7,8,9)
        dp = [0]*(days[-1]+1) # dp=[0]*(9 + 1)=[0,0,0,0,0,0,0,0,0,0]    
#         days = set(days) 없어도 됨. 이미 days가 값 순서대로 입력으로 들어오고 중복되지 않으므로 주석 처리함     
        
        for i in range(1,len(dp)):  #for i in range(1, 10)
            #i=1~10 
            if i in days:
                #i의 범위 안에 days가 있을 경우(1,5,6,7,8,9)
                #min(1일권 값, 7일권 값, 30일권 값) ->3중에 minimum cost 를 찾아서 갱신
                #이때 dp리스트에서 각각 1일전 7일전 30일전 값을 참고해서 어떤 값이 더 유리한지 판단한다.
                
                dp[i] = min(dp[max(i-1,0)]+costs[0],dp[max(i-7,0)]+costs[1],dp[max(i-30,0)]+costs[2])
                #i의 범위 안에 days가 없을 경우(2,3,4) 
            else:
                dp[i]=dp[i-1] #dp=[0,2,2,2,2,4,6,7,9,9]
                
        return dp[-1] #dp[-1]=9
