from collections import deque

def bfs(start, maps):
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    queue = deque()                     # https://excelsior-cjh.tistory.com/96
    queue.append(start)
    while queue:                        # 빈 list, 빈 que는 False가 된다.
        y, x, cnt = queue.popleft()
        maps[y][x] = 0                  # Point! 이미 방문한 곳 처리는 벽으로 만들어 버린다!
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            # BFS를 사용하므로, 가장 처음 발견하면, 그 cnt를 return하면 된다.
            if ny == len(maps)-1 and nx == len(maps[0])-1:
                return cnt + 1

            # 빈 공간을 만났다면,
            elif 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1: 
                maps[ny][nx] = 0
                queue.append((ny, nx, cnt+1))
    return -1

def solution(maps):
    # 첫 위치는, map[0][0]이며, count=1로 시작한다. 
    return bfs((0,0,1), maps) 
