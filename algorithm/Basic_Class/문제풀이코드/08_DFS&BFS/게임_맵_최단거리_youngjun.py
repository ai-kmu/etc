from collections import deque

def solution(maps):
  
    # 맵, visited, queue 초기화
    N, M = len(maps), len(maps[0])
    visited = [[0] * len(maps[i]) for i in range(len(maps))]
    q = deque()
    
    # 시작점 queue에 넣어주고
    q.append((0,0))
    # visited 체크
    visited[0][0] = 1
    
    # 방향 설정
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    # BFS
    while q:
        
        r, c = q.popleft()
        
        for dr, dc in direction:
            nr = r + dr
            nc = c + dc
            if 0 <= nr <= N - 1 and 0 <= nc <= M - 1 and maps[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                # 이전 위치의 거리에 1을 더해줌으로서, 해당 단계의 거리를 구해준다.
                maps[nr][nc] = maps[r][c] + 1
                q.append((nr, nc))
    # 끝에 도달할 수 없으면 -1, 있으면 거리 그대로 반환
    if maps[N-1][M-1] > 1:
        return maps[N-1][M-1]
    else:
        return -1
