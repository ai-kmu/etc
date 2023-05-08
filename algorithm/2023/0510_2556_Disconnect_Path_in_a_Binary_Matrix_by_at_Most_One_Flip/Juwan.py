class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:

        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return True

            if x >= m or y >= n or grid[x][y] == 0:
                return False

            grid[x][y] = 0

            return dfs(x + 1, y) or dfs(x, y + 1)

        if not dfs(0, 0):
            return True

        grid[0][0] = 1
        
        if not dfs(0, 0):
            return True

        return False
