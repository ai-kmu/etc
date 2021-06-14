class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        
        def dfs(i, j):
            if i<0 or i >=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == "0": 
                return
            
            grid[i][j] = "0" #  visited된 곳은 0dmfh
            dfs(i+1, j) # 동서남북으로 dfs 적용
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1": # 현재 위치가 land면
                    dfs(i, j) # dfs 탐색
                    count += 1  # land 개수 카운트
        return count
                    
        
