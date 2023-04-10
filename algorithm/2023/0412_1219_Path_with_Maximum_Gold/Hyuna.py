# 테케 걸림 
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0

        # 상하좌우
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        m = len(grid)
        n = len(grid[0])

        def dfs(x, y, visited):
            nonlocal ans
            # 범위 벗어나거나 이미 왔던곳이거나 그리드에서 0이면 다음으로 
            if 0 < x <= m  or y < 0 or y >= n or visited[x][y] == 1 or grid[x][y] == 0:
                return 

            visited[x][y] = 1
            temp = grid[x][y]
            # 기존의 개수와 더 큰걸로 가져감 
            ans = max(temp, ans)

            # 상하좌우 이동 
            for i in range(len(dx)):
                dfs(x + dx[i], y + dy[i], visited)
            
            visited[x][y] = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    visited = [[0] * m] * n
                    dfs(i, j, visited)
        return ans
