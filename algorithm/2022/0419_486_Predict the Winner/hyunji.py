'''
- player1이 nums[i]~nums[j] 배열에서 nums[i] or nums[j] 를 선택 (i < j)
   1. player1이 nums[i]를 선택했다면, player2는 nums[i+1]~nums[j] 배열에서 nums[i+1] or nums[j]를 선택함
   2. player2이 nums[j]를 선택했다면, player2는 nums[i]~nums[j-1] 배열에서 nums[i] or nums[j-1]를 선택함 
- player1, player2는 모두 score가 최적화(최대)되는 선택을 하게 됨 -> dp로 풀어야하는 문제

재귀식
- base case: Dp[i][i] = nums[i] (i == j)
- Dp[i][j] = max(nums[i] - Dp[i+1][j], nums[j] - Dp[i][j-1])  (1 <= i < j < n)
'''

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # 2차원 dp 배열 선언
        Dp = [[0 for col in range(n)] for row in range(n)]
        
        # base case
        for i in range(n):
            Dp[i][i] = nums[i]
        
        for diagnol in range(1, n):
            for i in range(n-diagnol):
                # 대각선으로 값을 채워나감(1 <= i < j < n)
                j = i + diagnol
                
                # player1에게 nums[i]와 nums[j] 중 최적의 선택으로 dp 배열을 채워나감
                Dp[i][j] = max(nums[i] - Dp[i+1][j], nums[j] - Dp[i][j-1])
                
        return Dp[0][n-1] >= 0
                
