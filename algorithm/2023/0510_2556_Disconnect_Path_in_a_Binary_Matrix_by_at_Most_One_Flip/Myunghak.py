# 그냥 첫번째 dfs 로 경로 탐색을 한번 한 후(이 때 지나간 경로는 표시함)
# 해당 경로를 지나지 않고 가는 다른 경로가 있는지 찾기

class Solution:
    def isPossibleToCutPath(self, grid):
        m, n = len(grid), len(grid[0])
        visit = [[False] * n for _ in range(m)]

        def dfs(x, y, visit):
            if x == m - 1 and y == n - 1:
                visit[x][y] = False
                return True

            for dx, dy in [(1, 0), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if new_x < m and new_y < n and not visit[new_x][new_y]  and grid[new_x][new_y]:
                    visit[new_x][new_y] = True
                    if dfs(new_x, new_y, visit):
                        return True

            return False

        dfs(0,0, visit)
        return not dfs(0,0, visit)
