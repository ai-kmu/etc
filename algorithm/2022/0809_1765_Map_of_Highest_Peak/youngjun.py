class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        cols, rows = len(isWater[0]), len(isWater)

        out_mat = [[-1] * cols for _ in range(rows)]

        visited = [[0] * cols for _ in range(rows)]

        bfs_q = deque()

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    out_mat[i][j] = 0
                    visited[i][j] = 1
                    bfs_q.append((j, i))

        def bfs(out_mat, visited, bfs_q):

            direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            while bfs_q:

                x, y = bfs_q.popleft()

                for dx, dy in direct:
                    nx = x + dx
                    ny = y + dy

                    if (nx < 0 or nx >= cols) or (ny < 0 or ny >= rows):
                        continue

                    if 0 <= nx <= cols and 0 <= ny <= rows and visited[ny][nx] == 0:
                        out_mat[ny][nx] = out_mat[y][x] + 1
                        visited[ny][nx] = 1
                        bfs_q.append((nx, ny))

            return out_mat

        return bfs(out_mat, visited, bfs_q)
