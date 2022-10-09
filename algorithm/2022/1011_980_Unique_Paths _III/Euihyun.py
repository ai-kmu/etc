# dfs 해보려고 했는데 실패

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m = len(grid)
        n = len(grid[0])
        
        # 시작점 찾기
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y =i, j

                    
