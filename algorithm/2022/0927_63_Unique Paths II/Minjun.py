class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        
        # 예외처리
        if obstacleGrid[0][0] == 1:
            return 0

        # 예외처리
        if len(obstacleGrid) == 1 or len(obstacleGrid[0]) == 1:
            for i in range(len(obstacleGrid)):
                for j in range(len(obstacleGrid[0])):
                    if obstacleGrid[i][j] == 1:
                        return 0
            return 1
        
        # 상단 1 채우기
        for i in range(len(obstacleGrid[0])):
            dp[0][i] = 1
            
        # 좌단 1채우기
        for i in range(len(obstacleGrid)):
            dp[i][0] = 1
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    continue
                
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    
                    continue
                
                # 내부 matix
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
