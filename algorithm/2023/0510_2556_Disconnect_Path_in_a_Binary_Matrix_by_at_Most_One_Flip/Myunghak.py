# 그냥 첫번째 dfs 로 경로 탐색을 한번 한 후(이 때 지나간 경로는 표시함)
# 해당 경로를 지나지 않고 가는 다른 경로가 있는지 찾기

class Solution:
    def isPossibleToCutPath(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(x, y, grid):
            if x == m - 1 and y == n - 1:
                grid[x][y] = 1
                return True

            for dx, dy in [(1, 0), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if new_x < m and new_y < n and grid[new_x][new_y]:
                    grid[new_x][new_y] = 0
                    if dfs(new_x, new_y, grid):
                        return True

            return False
        
        # 2번다 무사히 도착하면 안됨
        return not(dfs(0,0, grid) and dfs(0,0, grid))
