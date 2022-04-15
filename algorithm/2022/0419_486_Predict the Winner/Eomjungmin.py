
# 1. 2-D dynamic programming
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))] # 2차원 dp 선언
        
        # dp로 풀 때의 작은 부분: 맨 오른쪽에서 부분으로 취했을 때 player1이 선택 할 수 있는 최대 effective score
        for i in range(len(nums)-1,-1,-1): # 행은 역순으로 진행
            for j in range(i, len(nums)): # 열은 현재 행 숫자부터 마지막 열까지 진행
                if  i==j: # 대각 요소는 nums값 대입
                    dp[i][j] = nums[i]
                else: # 대각 요소가 아닌 곳은 player1이 선택할 수 있는 최대 effective score 계산한 결과 대입
                    dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][len(nums)-1] >= 0

    
# 2. 1-D dynamic programming
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # 1-D Dynamic programming
        dp = [0 for _ in range(len(nums))] # 1차원 dp 선언
        for i in range(len(nums)-1,-1,-1):
            for j in range(i, len(nums)):
                if  i==j:
                    dp[i] = nums[i]
                else:
                    dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
        return dp[-1] >= 0
