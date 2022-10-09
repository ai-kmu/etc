class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        m = len(grid)
        n = len(grid[0])
        
        start_x = None
        start_y = None
        visited = [[False]*n for i in range(m)]
        blocks = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == -1:
                    blocks += 1  
     
        answer = []
        
        def dfs(x, y, d):
            if grid[x][y] == -1:
                return

            if grid[x][y] == 2:
                answer.append(d)
                return
            
            for i, j in zip(dx, dy):
                if 0 <= x - i < m and 0 <= y - j < n and not visited[x - i][y - j]:
                    visited[x - i][y - j] = True
                    dfs(x - i, y - j, d + 1)
                    visited[x - i][y - j] = False
        
        visited[start_x][start_y] = True
        dfs(start_x, start_y, 1)
                
        return answer.count(m*n - blocks)
