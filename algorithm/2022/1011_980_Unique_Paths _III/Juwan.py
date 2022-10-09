from copy import deepcopy

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
        
        def dfs(x, y, d, maps):
            if maps[x][y] or grid[x][y] == -1:
                return
            maps[x][y] = True
            if grid[x][y] == 2:
                answer.append(d)
                return
            
            for i, j in zip(dx, dy):
                temp = deepcopy(maps)
                if 0 <= x - i < m and 0 <= y - j < n:
                    dfs(x - i, y - j, d + 1, temp)
            
        dfs(start_x, start_y, 1, visited)
                
        return answer.count(m*n - blocks)
