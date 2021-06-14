m = len(grid)
n = len(grid[0])
dq = deque()
islands = 0
for i in range(m):
    for j in range(n):
        # 만약 현재 노드가 "1"일 경우 island를 1 더해주고 방문한 노드들을 담아두는 deque에 i,j값을 넣어줌
        if grid[i][j] == '1':
            islands += 1
            dq.append([i, j])
            #방문한 노드마다 "-1"로 변
            grid[i][j] = '-1'

            while dq:
                
                x, y = dq.popleft()
                # 현재 위치에서 윗부분을 탐색
                if x - 1 >= 0:
                    if grid[x - 1][y] == '1':
                        grid[x - 1][y] = '-1'
                        dq.append([x - 1, y])
                        
                # 현재 위치에서 왼쪽을 탐색
                if y - 1 >= 0:
                    if grid[x][y - 1] == '1':
                        grid[x][y - 1] = '-1'
                        dq.append([x, y - 1])
                        
                # 현재 위치에서 아래부분을 탐색
                if x + 1 < m:
                    if grid[x + 1][y] == '1':
                        grid[x + 1][y] = '-1'
                        dq.append([x + 1, y])
                        
                # 현재 위치에서 오른쪽을 탐색
                if y + 1 < n:
                    if grid[x][y + 1] == '1':
                        grid[x][y + 1] = '-1'
                        dq.append([x, y + 1])
return islands
