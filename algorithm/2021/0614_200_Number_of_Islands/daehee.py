class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.i_n = 0
        self.grid = grid
        self.l_y, self.l_x = len(grid), len(grid[0])
        
                
        for yy in range(self.l_y):
            for xx in range(self.l_x):
                if self.grid[yy][xx]=="1":    #1이면 섬 갯수 늘리고 거기부터 dfs 시작
                    self.i_n += 1
                    self.dfs(yy, xx)
                    # print(self.grid, self.i_n, yy, xx)
        return self.i_n
    
    def dfs(self, y, x):      # dfs로 이어져있는것들 다 마크
        if x<0 or y<0 or y>=self.l_y or x>=self.l_x: return
        if self.grid[y][x]=="1":
            self.grid[y][x] = "0"
            self.dfs(y-1, x)
            self.dfs(y+1, x)
            self.dfs(y, x-1)
            self.dfs(y, x+1)
