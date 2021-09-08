class Solution(object):
    def maxAreaOfIsland(self, grid):
        def search(i, j):
            if (i < 0 or j < 0 or len(grid) <= i or len(grid[0]) <= j or grid[i][j] ==0): ## 그리드 넘거나 0이면 탐색 x
                return 0
            grid[i][j] = 0 ## 한번 방문 하면 0으로
            return 1 + search(i-1,j) + search(i,j-1) + search(i+1,j) + search(i,j+1) ## 상하좌우 탐색
        ans = 0
        for i in range(len(grid)): ## 모든 그리드 탐색
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, search(i, j)) ## 가장 넓은 지역으로
        return ans 
