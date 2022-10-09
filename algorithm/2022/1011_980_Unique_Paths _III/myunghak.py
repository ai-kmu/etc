class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        empty_space = r * c - 1
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == -1:
                    empty_space -= 1
                elif grid[i][j] == 2:
                    target = (i, j) 
                    
        flag = [[0] *c for _ in range(r)]
        self.ans = 0
        def dfs(walk, y,x, flag):
            if 0<=y<r and 0<= x < c and flag[y][x] == 0 and (grid[y][x] != -1):
                if (y, x) == target:
                    if walk == empty_space:
                        self.ans +=1
                    return
                
                flag[y][x] = 1
                dfs(walk+1, y-1, x, flag)
                dfs(walk+1, y+1, x, flag)
                dfs(walk+1, y, x-1, flag)
                dfs(walk+1, y, x+1, flag)
                flag[y][x] = 0
                
        dfs(0, start[0], start[1], flag)
        
        return self.ans
