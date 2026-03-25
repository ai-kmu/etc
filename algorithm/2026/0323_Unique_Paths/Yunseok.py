from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited_list = [[0 for j in range(n)] for i in range(m)]
        cnt_val = 0
        
        @cache
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1

            paths = 0

            for next_dir in [[0, 1], [1, 0]]:
                next_y = i + next_dir[0]
                next_x = j + next_dir[1]

                if next_y < m and next_x < n:
                    paths += dfs(next_y, next_x)
                else:
                    continue

            return paths

        return dfs(0, 0)
