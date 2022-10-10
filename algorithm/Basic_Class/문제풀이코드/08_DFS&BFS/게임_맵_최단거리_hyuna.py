from collections import deque
def solution(maps):
    
    m = len(maps)
    n = len(maps[0])
    dq = deque()
    dq.append((0,0))
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    while dq:
        # 현재 좌표 꺼내오기
        x, y = dq.popleft()
        
        # 상하좌우 조희    
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 정상적인 범위 안에 속하고 아직 조회하지 않은 경우 이전 칸의 이동 수에 1을 더해 넣어준다
            # 다음 조회를 위해 덱에 추가 한다
            if 0<=nx<m and 0<=ny<n and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                dq.append((nx, ny))
            else:
                continue
    
    # 마지막 칸이 1이라면 움직임이 없었던 것이므로 -1 리턴
    return -1 if maps[m-1][n-1] == 1 else maps[m-1][n-1]
