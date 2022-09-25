class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0])]*len(obstacleGrid)
        
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    continue                
#                 # 상단
                if i == 0:
                    dp[i][j] = dp[i][j-1] + 1
                
                print(dp, i, j)
                # 좌단
                # if j == 0:
                #     dp[i][j] = dp[i-1][j] + 1
                #     print(dp, "i", i, "j", j)
#                 # 내부 matix
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
