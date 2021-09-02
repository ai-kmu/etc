import sys
sys.setrecursionlimit(30000)
def dfs(x, y, grid):
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] == 0:
            return 0    #0인 지역은 0을 반환하여 cnt가 증가하지 않음
        grid[y][x] = 0
        return dfs(x-1, y, grid) + dfs(x+1, y, grid) + dfs(x, y-1, grid) + dfs(x, y+1, grid) + 1  #1인 지역을 방문하면 cnt를 1 증가

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:   #1인 지역이 나타나면 dfs 수행 후 max값을 비교
                    cnt = max(dfs(j, i, grid), cnt)
        return cnt
