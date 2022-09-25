class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp를 활용한 풀이
        # 현재 위치가 장애물이면 가능한 path의 수는 0
        # 장애물이 아니면 위쪽과 왼쪽의 path의 수를 합한 것
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        # base case
        # 제일 위의 행과 제일 왼쪽 열은
        # 출발점에서 시작하여 장애물이 없으면 1
        # 장애물을 만나는 순간 그 뒤는 0
        for i in range(m):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
        for i in range(1, n):
            if obstacleGrid[0][i]:
                break
            dp[0][i] = 1
        
        for row in range(1, m):
            for col in range(1, n):
                # 장애물을 만나지 않았을 경우
                # 초기값 0을 왼쪽 값과 오른쪽 값의 합으로 설정
                if not obstacleGrid[row][col]:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        # 최종 위치에서의 가능한 path의 수를 출력
        return dp[-1][-1]
