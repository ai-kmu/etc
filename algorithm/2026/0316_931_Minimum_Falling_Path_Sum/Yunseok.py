from functools import lru_cache

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        @lru_cache(None)
        def dfs(i, j):
            if j < 0 or j == n:
                return float('inf')
            if i == n - 1:
                return matrix[i][j]
            
            return matrix[i][j] + min(dfs(i + 1, j - 1), dfs(i + 1, j), dfs(i + 1, j + 1))

        return min(dfs(0, j) for j in range(n))
