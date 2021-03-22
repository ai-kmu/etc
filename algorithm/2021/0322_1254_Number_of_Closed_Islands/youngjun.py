class Solution(object):
    def closedIsland(self, grid):     
        def exclude(): # exclude 처리 
            
            for i in range(0, len(grid), 1):
                for j in range(0, len(grid[0]),1):
                    
                    if (i==0 or j==0 or i==len(grid)-1 or j == len(grid[0])-1) and grid[i][j] == 0:
                        dfs(i,j,1)
                        
        def dfs(r, c, val): # 인접한 부분을 확인하기 위한 dfs
            
            if grid[r][c] == 0:
                grid[r][c] = val
           
                if r+1 < len(grid) :
                    dfs(r+1,c,val)
                if c-1 >= 0:
                    dfs(r, c-1, val)
                if r-1 >= 0:
                    dfs(r-1, c, val)
                if c+1 < len(grid[0]):
                    dfs(r, c+1, val)

                    
        def printgrid(grid): #grid를 print
            
            for i in grid:
                print(i)
        exclude()
         
        closed_island = 0
        for i in range(0, len(grid), 1):

            for j in range(0, len(grid[0]), 1):
                
                if grid[i][j] == 0:
                    pass
                    dfs(i,j, grid)
                    closed_island+=1
        
        return closed_island
