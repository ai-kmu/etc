from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 시작점 방문 설정
    maps[0][0] = 0
    
    # BFS
    # q에는 현재 위치 (r, c)와 현재까지 움직인 거리가 담겨있다.
    # 리스트보다 튜플이 좀 더 빠르고 메모리가 적음
    q = deque([(0, 0, 1)])
    while q:
        r, c, path = q.popleft()
        
        # 종료 조건: 끝에 도달
        if r + 1 == n and c + 1 == m:
            return path
            
        # Index 검사 하고
        # 장애물 or visited이 아니면 추가 후 visited 처리
        if 0 < r and r < n and maps[r - 1][c]:
            q.append((r - 1, c, path + 1))
            maps[r - 1][c] = 0
        if 0 <= r and r < n - 1 and maps[r + 1][c]:
            q.append((r + 1, c, path + 1))
            maps[r + 1][c] = 0
        if 0 < c and c < m and maps[r][c - 1]:
            q.append((r, c - 1, path + 1))
            maps[r][c - 1] = 0
        if 0 <= c and c < m - 1 and maps[r][c + 1]:
            q.append((r, c + 1, path + 1))
            maps[r][c + 1] = 0
    
    # while 다 돌았다 = return 못 만났다 = 끝에 도달하지 못했다
    return -1
    
