def solution(maps):

    directions = [[0,1],[1,0],[0,-1],[-1,0]]  # 방향들(RIGHT, UP, LEFT, DOWN)
    path = []  # 지나온 경로 저장할 리스트

    path.append([0,0,1])  # (0,0)에서 시작, 총 1개 블록 거침

    answer = -1

    while path:
        x, y, count = path.pop(0)  # 현재 x좌표, 현재 y좌표, 거쳐온 블록 수
        maps[x][y] = 0  # 이미 도달한 블록은 0으로 변경

        for dx, dy in directions:  # 모든 방향들에 대해서
            cx, cy = x + dx, y + dy  # 이동(x,y좌표 변경)

            if cx == len(maps)-1 and cy == len(maps[0])-1:  # 이번에 도달할 곳이 적진인 경우
                answer = count + 1  # 1번 더 가야 적진이므로 총 거쳐온 블록 수는 count에 1 더한
                return answer
            elif 0 <= cx <= len(maps)-1 and 0<= cy <= len(maps[0])-1 and maps[cx][cy]==1:
            # 아직 적진에 도달하지 못하였고 이번 도달할 곳이 벽이 아닌 경우
                maps[cx][cy] = 0  # 이번 도달할 곳을 0으로 변경
                path.append([cx,cy,count+1])  # 경로에 추가

    return answer  # 따라서 도달하지 못하면 -1 return
    
    
