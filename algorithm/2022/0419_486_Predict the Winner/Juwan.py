class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
        dp로 푸는 문제.
        
        문제를 해석하자면, player 1이 어떠한 것을 고르는가에 따라 승패가 결정.
        하지만, player 1이 이길 수 있는 상황만 만들어지면 된다.
        
        """
        
        dp = [0] * len(nums) # dp를 초기화
        
        
        for i in range(len(nums), -1, -1): # 역방향으로 loop를 돌아간다. 
            
            
            for j in range(i, len(nums)):
                
                if i == j:
                    
                    dp[i] = nums[i] # dp에 값을 채워놓는 용도
                    
                else:
                    
                    x = nums[i] - dp[j]
                    y = nums[j] - dp[j - 1]
                    dp[j] = max(x, y)
                    
        return dp[-1] >= 0
      
 """
 test case 가 [1,5,2,4,6]
 dp는
 
dp :  [0, 0, 0, 0, 6]
dp :  [0, 0, 0, 4, 6]
dp :  [0, 0, 0, 4, 2]
dp :  [0, 0, 2, 4, 2]
dp :  [0, 0, 2, 2, 2]
dp :  [0, 0, 2, 2, 4]
dp :  [0, 5, 2, 2, 4]
dp :  [0, 5, 3, 2, 4]
dp :  [0, 5, 3, 3, 4]
dp :  [0, 5, 3, 3, 3]
dp :  [1, 5, 3, 3, 3]
dp :  [1, 4, 3, 3, 3]
dp :  [1, 4, -2, 3, 3]
dp :  [1, 4, -2, 6, 3]
dp :  [1, 4, -2, 6, 0]
 
 """
