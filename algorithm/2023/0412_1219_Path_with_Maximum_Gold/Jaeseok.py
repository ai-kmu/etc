class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        self.answer = 0

        # 백트래킹
        def dfs(x, y, gold):
            # 움직일 방향 설정
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            # 가장 많이 돈을 벌었을 때가 정답
            self.answer = max(self.answer, gold)
            # 위,아래,좌,우로 움직일 수 있기 때문에 4번 반복
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # grid 밖으로 나가는 경우를 제외
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                # 이미 방문한 경우거나 돈이 없는 경우를 제외
                if visited[nx][ny] or grid[nx][ny] == 0:
                    continue
                # 방문 처리 후 깊이 우선 탐색
                visited[nx][ny] = True
                dfs(nx, ny, gold + grid[nx][ny])
                visited[nx][ny] = False

        # 어느 위치에서든 시작할 수 있기 때문에 grid 전체를 순회하면서
        # grid가 0이 아닌 지점을 시작점으로 삼고 탐색 시작
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    visited[i][j] = True
                    dfs(i, j, grid[i][j])
                    visited[i][j] = False

        return self.answer
