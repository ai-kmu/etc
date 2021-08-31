class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_out = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                current_coord = [i, j]
                if grid[i][j] == 1:
                    max_out = max(max_out, self.dfs(current_coord, grid))
                    
        return max_out
        
        
        
    def check_valid(self, i, j, grid):
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0):
            return 0
        else:
            return 1
        
        
    def dfs(self, current_coord, grid):
        isValid = self.check_valid(current_coord[0], current_coord[1], grid)
        if isValid == 1:
            i = current_coord[0]
            j = current_coord[1]
            grid[i][j] = 0
            total = 1
            total = total + self.dfs([i + 1, j], grid)
            total = total + self.dfs([i, j + 1], grid)
            total = total + self.dfs([i - 1, j], grid)
            total = total + self.dfs([i, j - 1], grid)
            
            return total
        
        else:
            return 0
