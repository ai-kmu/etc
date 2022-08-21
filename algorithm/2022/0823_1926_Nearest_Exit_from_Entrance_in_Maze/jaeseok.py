from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # 움직일 수 있는 방향 지정
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        # 미로의 크기
        lim_x = len(maze)
        lim_y = len(maze[0])
        # 큐 선언하고 현재 위치, 움직인 거리를 큐에 넣어주고 움직일 수 없느 곳으로 만들어줌
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = "+"
        def bfs():
            while q:
                # 현재 위치와 움직인 거리를 pop
                x, y, steps = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 현재 위치에서 각 방향으로 움직이면서 움직일 수 있는 위치인지 확인
                    if nx >= 0 and ny >= 0 and nx < lim_x and ny < lim_y and maze[nx][ny] == ".":
                        # 만약에 출구 부분에 도착하였으면 가장 빠른 경로의 출구이므로 현재까지의 움직인 거리 +1을 return
                        if nx == 0 or nx == lim_x - 1 or ny == 0 or ny == lim_y - 1:
                            return steps + 1
                        # 아니라면 움직인 위치를 더 이상 움직일 수 없게 만듦
                        maze[nx][ny] = "+"
                        # 움직인 위치와 움직인 거리를 큐에 넣어줌
                        q.append((nx, ny, steps + 1))
        
        answer = bfs()
        # bfs를 전부 돌 때까지 answer에 값이 안 들어갔다면 미로를 탈출 할 수 없는 것이므로 -1을 return
        return answer if answer is not None else -1       
