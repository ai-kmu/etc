class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        # dp에서 for loop에서 사용할 loop의 횟수.
        
        dp = [0 for i in range(n+1)]
        
        """
        example : days = [1,4,6,7,8,20], costs = [2,7,15] 으로 가정했을 때,
        
        처음 dp 배열은
        
        print(dp) = [0, 0, 0, 0, 0, 0, 0]
        
        """        
        
        
        pass_7 = 0 # days 배열에서 7일 패스권의 포인터 개념임. 현재로부터 7일전.
        pass_30 = 0 # 위의 7일 패스권 처럼 30일 패스권의 포인터 개념.
        
        # days의 요소 하나씩마다 while문 2번이나 사용하여 시간적으로 비효율적
        # 결국엔 days 안 요소값이 7보다 작은 경우, 30보다 작은 경우로 구현하는게 더 좋지 않을까 하는 생각이 듦.       
        # dp[i] = min(dp[i-1] + costs[0],dp[max(0,i-7)] + costs[1], dp[max(0,i-30)]+costs[2])
        for i in range(n):
          
            print("days[i] : ", days[i])
            
            
            while days[i] > days[pass_7] + 6:
                print("days[pass_7] : ", days[pass_7])
                pass_7 += 1
            while days[i] > days[pass_30] + 29:
              
                print("days[pass_30] : ", days[pass_30])

                pass_30 += 1
                
            dp[i+1] = min(dp[i] + costs[0], dp[pass_7] + costs[1], dp[pass_30] + costs[2])
            print(dp)
            
            
            """
            days[i] :  1
            days[i] :  4
            days[i] :  6
            days[i] :  7
            days[i] :  8
            days[pass_7] :  1
            days[i] :  20
            days[pass_7] :  4
            days[pass_7] :  6
            days[pass_7] :  7
            days[pass_7] :  8
            [0, 2, 4, 6, 7, 9, 11]
            
            이런식으로 진행이 된다. 
            dp[i+1] = min(dp[i] + costs[0], dp[pass_7] + costs[1], dp[pass_30] + costs[2])
            에 의해 어떤 Pass 권을 사용해야 가장 저렴한지 판별하는 방식이다.
            
            
            """
            
            
            
            
            
            
        return dp[-1]
      
