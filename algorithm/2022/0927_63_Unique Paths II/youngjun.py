class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # 기록 초기화
        dp = [[0] * n for i in range(m)]

        # down 가장자리 초기화
        for i in range(m):
            # 장애물이 없으면 1을 기록
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            # 장애물이 있으면 0을 기록하고 break
            else:
                dp[i][0] = 0
                break

        # left 가장자리 초기화
        for j in range(n):
            # 장애물이 없으면 1을 기록
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            # 장애물이 있으면 0을 기록하고 break
            else:
                dp[0][j] = 0
                break

        # 가장자리 안쪽 기록 시작
        for i in range(1, m):
            for j in range(1, n):
                # 장애물이 있을 경우 0을 기록
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                # 장애물이 없을 경우 왼쪽과 윗쪽 값의 합을 기록
                else:
                    dp[i][j] = dp[i][j -1] + dp[i - 1][j]

        return dp[m-1][n-1]
