from collections import defaultdict

class Solution:
    def isPossibleToCutPath(self, grid):
        m, n = len(grid), len(grid[0])
        paths_dict = defaultdict(int)
        visit = [[False] * n for _ in range(m)]

        def dfs(x, y, visit, total_path, path_num):
            if x == m - 1 and y == n - 1:
                # print(total_path)
                for d in total_path:
                    paths_dict[d] += 1

                return path_num + 1

            for dx, dy in [(1, 0), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if new_x < m and new_y < n and not visit[new_x][new_y]  and grid[new_x][new_y] == 1:
                    visit[new_x][new_y] = True
                    path_num = dfs(new_x, new_y, visit, total_path + [(new_x, new_y)], path_num )
                    visit[new_x][new_y] = False
            return path_num

        visit[0][0] = True
        path_num = dfs(0,0, visit, [(0,0)], 0)
        # print(paths_dict)
        paths_dict[(0,0)] = 0
        paths_dict[(m-1,n-1)] = 0

        for k in paths_dict:
            if paths_dict[k] == path_num:
                return True
        return False
