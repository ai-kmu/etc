from collections import deque

action_x = [0, 0, 1, -1]
action_y = [1, -1, 0, 0]

N, M = map(int, input().split())
# 미로 10101010
maze = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
# 거리를 기록
dist = [[0] * M for _ in range(N)]

q = deque()
# 첫 지점 세팅
q.append((0, 0))
visited[0][0] = True
dist[0][0] = 1

# deque에 원소가 남아있는 동안 반복
while q:
    # 앞에서 pop. O(1)
    x, y = q.popleft()
    for k in range(4):
        next_x, next_y = x + action_x[k], y + action_y[k]
        if 0 <= next_x < N and 0 <= next_y < M:
            if not visited[next_x][next_y] and maze[next_x][next_y] == 1:
                q.append((next_x, next_y))
                dist[next_x][next_y] = dist[x][y] + 1
                visited[next_x][next_y] = True

print(dist[N - 1][M - 1])
