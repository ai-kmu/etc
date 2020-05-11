def solution(maps):
    answer = 0
    directs = [(0,1),(1,0),(0,-1),(-1,0)] #이동방향 리스트
    n = len(maps) - 1
    m = len(maps[0]) - 1 #맵의 크기
    queue = []
    queue.append([0,0,1]) #게임의 시작위치, count=1로 시작
    
    while queue:
        x, y, count = queue.pop(0) #현재위치
        #경로마다 count수가 다르기 때문에 한 리스트로 묶어준다
        maps[x][y] = 0 #지나간 길 벽으로 만들기
        for dx, dy in directs: #상,하,좌,우로 이동
            px, py = x + dx, y + dy
            #상대팀 진영에 먼저 도달한 경로를 출력
            if px == n and py == m:
                return count + 1
            #최단거리이므로 지나간 길은 벽으로 만들기
            if 0 <= px <= n and 0 <= py <= m and maps[px][py] == 1:
                maps[px][py] = 0
                queue.append([px, py, count+1])
    return -1
