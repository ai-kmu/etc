# 정답
def solution(maps):
    # 오른쪽, 아래쪽, 왼쪽, 위쪽 방향으로의 이동을 향하기 위한 배열
    dirs = [(0,1), (-1, 0), (0, -1), (1, 0)]
    # bfs 탐색을 위한 queue
    queue = list()
    # 0,0위치에서 시작이며, 지나온 블럭은 자기자신을 포함한 1
    queue.append((0,0,1))
    # queue가 빌 때까지
    while queue:
        # 가는 방향의 row, col그리고 가는 데 소비한 cost
        row, col, cost = queue.pop(0)
        # 이미 방문한 위치는 벽으로 취급
        maps[row][col] = 0
        # 모든 방향을 돌아봄
        for r, c in dirs:
            # 이동한 위치를 담는 tmp_r, tmp_c
            tmp_r, tmp_c = row + r, col + c
            # tmp_r, tmp_c가 적의 위치라면 이동한 칸수 1을 더한 cost를 return
            if tmp_r == len(maps)-1 and tmp_c == len(maps[0])-1:
                return cost+1
            # 행과 열의 위치는 0이상, n,m이하여야 하며, 벽이 아닌 경우에한해서
            elif 0 <= tmp_r < len(maps) and 0 <= tmp_c < len(maps[0]) and maps[tmp_r][tmp_c]:
                # 지나온 길은 벽으로
                maps[tmp_r][tmp_c] = 0
                # 큐에 지난 블럭과 cost를 저장
                queue.append((tmp_r, tmp_c, cost+1))
    return -1
    
# 수정중
def solution(maps):
    answer = 0
    row = len(maps)
    col = len(maps[0])
    # 오른, 아래, 왼, 위쪽 방향 리스트
    dirs = [(0,1), (-1, 0), (0, -1), (1, 0)]
    
    # 각 위치로 가기 위한 비용 지도
    cost = [[0]*col]*row
    
    for r in range(row):
        for c in range(col):
            # 0,0 즉 시작점인 경우 cost는 1로 설정
            if r==0 and c==0:
                cost[r][c] == 1
                continue
            # 벽인 경우는 패스
            if maps[r][c] == 0:
                continue
            # 방향 돌면서
            for i, j in dirs:
                tmp_r, tmp_c = r + i, c + j
                if tmp_r == len(maps)-1 and tmp_c == len(maps[0])-1:
                    break
                # 행과 열의 위치는 0이상, n,m이하여야 하며, 벽이 아닌 경우에한해서
                elif 0 <= tmp_r < len(maps) and 0 <= tmp_c < len(maps[0]) and maps[tmp_r][tmp_c]:
                    cost[r][c] = 1 + cost[tmp_r][tmp_c]
    if cost[row-1][col-1] == 0:
        answer = -1
    else:
        answer = cost[row-1][col-1]
    print(cost)
    return answer
