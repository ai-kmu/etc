from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        answer = 0
        N = len(maze)
        M = len(maze[0])
        
        q = deque()
        
        # 입구 index와 distance를 0으로 초기화해서 넣어줌
        q.append([entrance[0], entrance[1], 0])
        visited = [[0]*M for _ in range(N)]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        # 입구 방문 처리
        visited[entrance[0]][entrance[1]] = 1

        while q:
            x, y, d = q.popleft()
            
            # 4방향으로 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nd = d + 1
                
                # 이동한 index가 범위 밖으로 나가지 않고, 그 지점이 아직 방문하지 않은 곳인 경우
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                    if maze[nx][ny] == '.':
                        
                        # 출구인 경우
                        if nx == 0 or ny == 0 or nx == N-1 or ny == M-1:
                            return nd

                        q.append([nx, ny, nd])
                        visited[nx][ny] = 1

        return -1
            
