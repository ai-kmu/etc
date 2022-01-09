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
      
