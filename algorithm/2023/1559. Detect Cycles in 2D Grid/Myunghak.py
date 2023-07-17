# 답보고 풀었어요
# 풀이 안해주셔도 되요

class Solution:
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and self.dfs(grid, visited, i, j, -1, -1):
                    return True
        return False
    
    def dfs(self, grid, visited, i, j, pi, pj):
        m, n = len(grid), len(grid[0])
        visited[i][j] = True
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and grid[i][j] == grid[ni][nj] and ((visited[ni][nj] and (ni, nj) != (pi, pj)) or (not visited[ni][nj] and self.dfs(grid, visited, ni, nj, i, j))):
                return True
        return False
