class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        # dptable 초기화
        dptable= [[0 for _ in range(col)] for _ in range(row)]
        # 위ㆍ왼벽 값 초기화
        for i in range(col):
            if obstacleGrid[0][i] == 1:
                break
            dptable[0][i] = 1
        for j in range(row):
            if obstacleGrid[j][0] == 1:
                break
            dptable[j][0] = 1
        
        # dp
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dptable[i][j] = dptable[i - 1][j] + dptable[i][j - 1]
        
        return dptable[row - 1][col - 1]
                    
        
