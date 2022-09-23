class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1: # 처음부터 막혔다면 return 0
            return 0
        
        switch = 1
        
        for i in range(m):
            
            if obstacleGrid[i][0] == 1: # 세로축 왼쪽 가장자리에서 장애물을 만나는 순간 그 뒤로는 모두 0으로 초기화
                switch = 0
            obstacleGrid[i][0] = switch # 만약 장애물이 가장자리에 없으면 1로 초기화
        
        switch = 1
        
        for i in range(1, n): # 가로축 위쪽 가장자리에 대한 코드. 위와 동일함
            
            if obstacleGrid[0][i] == 1: 
                switch = 0
            obstacleGrid[0][i] = switch
            
        
        for i in range(1, m): # DP로 해결
            for j in range(1, n):
                
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1] if obstacleGrid[i][j] != 1 else 0

        return obstacleGrid[-1][-1]
                
