class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # 2명의 player가 게임함
        # player 1 and player 2가 nums를 가지고 게임
        # p1이 first, score 0에서 시작
        # nums에서 각각 끝을 가져옴 nums[0] or nums[nums.length -1]
        # game은 element 없을 때까지 진행
        # player 1이 이길 수 있다면 true
        # 동점이이어도 true, 최적의 플레이를 하고 있다고 가정
        
        n, dp = len(nums), nums.copy()        
        
        # 점수차이가 최대가 나도록 dp 탐색
        for span in range(1, n):
            for i in range(n-span): 
                dp[i] = max(nums[i]-dp[i+1], nums[i+span]-dp[i])
                
        return dp[0] >= 0
