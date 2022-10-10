from collections import deque


def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    # 초기 위치는 (0,0)으로 고정
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            # 다음 갈 위치 지정
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 갈 위치가 map을 벗어나거나 벽이면 더 이상 진행하지 않음
            if (nx < 0 or ny < 0 or nx >= rows or
                    ny >= cols or maps[nx][ny] == 0):
                continue
            # map이 1인 곳은 아직 가지 않은 곳(visited의 역할도 겸함)이므로 한칸 더 간 거리로 넣어줌
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                # 다음 탐색을 위해 q에 위치를 넣어줌
                q.append((nx, ny))
    # 목표지점은 무조건 맨 오른쪽 아래, 만약에 도달하지 못했다면 1일 테므로 -1을 return
    return maps[-1][-1] if maps[-1][-1] != 1 else -1
