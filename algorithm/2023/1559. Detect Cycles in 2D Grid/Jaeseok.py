# 정답 확인했습니다 리뷰 x

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()

        def bfs(q, target):
            while q:
                x, y, path, prev = q.popleft()

                # 방문 처리
                visited.add((x, y))
                # 현재 순회하는 경로 추가
                path.add((x, y))

                # 다음 가능한 경로를 살펴보면서
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
                    # 다음 경로가 grid 밖을 벗어나지 않으면서 문자가 일치할 경우
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == target:
                        # 이미 방문한 적이 있는 곳 중에 바로 직전에 탐색한 곳이 아니라면 cycle
                        if (nx, ny) in path and (nx, ny) != prev:
                            return True
                        # 아직 방문한 적이 없다면 q에 추가하고 다음 탐색 시작
                        elif (nx, ny) not in path:
                            q.append((nx, ny, path, (x, y)))

            return False

        # 아직 방문하지 않은 가능한 모든 경우를 BFS 순회
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    # 한 번의 순회에 한 번의 큐를 사용
                    q = deque([(i, j, set(), (-1, -1))])
                    if bfs(q, grid[i][j]):
                        return True

        return False
