class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DP 방식으로 품
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        if obstacleGrid == [[0]]:
            return 1
        
        # 시작점에서 장애물이 있는 경우 도착할 방법이 없음
        if obstacleGrid[0][0] == 1:
            return 0
        
        # 2차원 dp에서 현재 지점의 dp값은 바로 위의 dp값과 바로 왼쪽의 dp값을 더한 것과 같음
        # 다만 첫행과 마지막행, 그리고 바로 윗행이 0번째 행인 경우 좀 다르게 dp값 계산해야 함
        for i in range(m):
            for j in range(n):
                # 시작점에서는 for문 안돌도록 continue
                if i == 0 and j == 0:
                    continue
                
                # 0번째 행에서의 dp값 계산
                if i == 0:
                    if j == 1 and obstacleGrid[i][j] != 1:
                        dp[i][j] = 1
                    elif j != 1 and obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i][j-1]
                
                # 마지막 행인 경우의 dp값 계산
                elif i == m-1:
                    if j == 0 and obstacleGrid[i][j] != 1:
                        if i-1 == 0 and obstacleGrid[i][j] != 1:
                            dp[i][j] = 1
                        elif i-1 != 0 and obstacleGrid[i][j] != 1:
                            dp[i][j] = dp[i-1][j]
                    elif j!= 0 and obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                        
                # 나머지 사이 행에서의 dp값 계산
                else:
                    if j == 0 and obstacleGrid[i][j] != 1:
                        if i-1 == 0 and obstacleGrid[i][j] != 1:
                            dp[i][j] = 1
                        elif i-1 != 0 and obstacleGrid[i][j] != 1:
                            dp[i][j] = dp[i-1][j]
                    elif j != 0 and obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
