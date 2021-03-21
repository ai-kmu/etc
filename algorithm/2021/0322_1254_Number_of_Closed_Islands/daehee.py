class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        
        def dfs(y,x, bunch):                              ## dfs로 색칠하기
            if h>y>-1 and w>x>-1:
                if grid[y][x]==0:
                    grid[y][x] = bunch
                    dfs(y-1,x, bunch)
                    dfs(y,x-1, bunch)
                    dfs(y+1,x, bunch)
                    dfs(y,x+1, bunch)
            
        
        for i in range(h):                                ## 바깥쪽에 있는 0들 1로 색칠하기 (완벽하게 1로 둘러싸일 수 없는 0)
            for j in range(w):
                if i==0 or i==h-1 or j==0 or j==w-1:
                    dfs(i,j,1)
        
        n_bunch = 0
        for i in range(1,h-1):                            ## 이어져있는 0들 찾을때마다 개수 세기
            for j in range(1,w-1):
                if grid[i][j]==0:
                    dfs(i,j,1)
                    n_bunch += 1
        
        return n_bunch
                
