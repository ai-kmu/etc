class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        # dp 테이블을 전부 0으로 초기화
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        # 첫번째 줄의 경로는 장애물을 만나기 전까지 유일하므로
        # row와 col의 첫 줄을 전부 돌면서 첫 번째 장애물을 만나기 전까지 계속 1로 초기화
        for row in range(rows):
            if obstacleGrid[row][0] == 0:
                dp[row][0] = 1
            else:
                break
        for col in range(cols):
            if obstacleGrid[0][col] == 0:
                dp[0][col] = 1
            else:
                break
        # 움직이는 경우의 수는 오른쪽과 왼쪽이므로 장애물 칸이 아니 경우 왼쪽과 위쪽까지의 경로의 수를 더해감
        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
        # 출구에서의 경로의 수가 정답
        return dp[rows - 1][cols - 1]
