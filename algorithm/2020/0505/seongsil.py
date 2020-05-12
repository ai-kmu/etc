def solution(maps):
    dirs = [(0,1), (1,0), (0,-1),(-1,0)]
    q = [(0,0,1)]

    while q:
        y, x, cnt = q.pop(0)
        maps[y][x] = 0
        for dy, dx in dirs:  # 4가지 방향 점검
            col, row = y+dy, x+dx
            if col == len(maps)-1 and row == len(maps[0])-1: # 최종 지점 도착
                return cnt + 1
        
            # 1인 블럭을 지나가는 경우 q에 저장
            elif 0 <= col < len(maps) and 0 <= row < len(maps[0]) and maps[col][row] == 1:
                maps[col][row] = 0
                q.append((col,row,cnt+1))
            print(q)
    return -1
        
        
