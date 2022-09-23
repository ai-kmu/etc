class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m x n grid, robot : [0][0], 
        # obstacle 1, path 0
        
        # edge case
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == -1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        answer = [[0 for _ in range(n)] for _ in range(m)] # dp 초기화
        
        # 첫번째 열과 행 초기화
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            answer[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            answer[0][i] = 1
        
        # 이후부터 path면 칸 업데이트, left와 up 칸의 정보를 더하면 됨
        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 0:
                    answer[r][c] = answer[r-1][c] + answer[r][c-1]

        return answer[-1][-1]
        
        
