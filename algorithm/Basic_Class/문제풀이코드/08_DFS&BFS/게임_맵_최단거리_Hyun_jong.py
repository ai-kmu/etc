from collections import deque
def solution(maps):
    answer = 0

    # 방향 지정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cols = len(maps)
    rows = len(maps[0])
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            
            # 방향 탐색
            for i in range(4):
                current_x = x + dx[i]
                current_y = y + dy[i]
                    
                # 예외 처리
                if current_x < 0 or current_x >= cols or current_y < 0 or current_y >= rows: 
                    continue

                # 거리 계산
                if maps[current_x][current_y] == 1:
                    maps[current_x][current_y] = maps[x][y] + 1
                    queue.append((current_x, current_y))

        return maps[cols-1][rows-1]

    answer = bfs(0, 0)
    if answer == 1:
        return -1 
    else:
        return answer
