def solution(places):
    
    def explore(i, j, distance = 0):
        nonlocal permit
        
        # 범위 밖
        if i < 0 or j < 0 or i >= len(place) or j >= len(place[0]):
            return
        
        # 맨하튼 거리 범위 밖
        if distance >= 3:
            return
        
        # 방문처리
        if visited == True:
            return
        visited[i][j] = True
        
        # 벽이면 안감
        if place[i][j] == 'X':
            return
        
        # 맨하튼거리안에 사람이 있으면
        if place[i][j] == 'P':
            permit = 0
            return        
        
        # 위배되었으면
        if permit == 0:
            return
        
        # 이동
        for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            explore(i+dy, j+dx, distance+1)

    answer = []
    
    # places탐색
    for place in places:
        
        visited = [[False for _ in place[0]] for _ in place]
        permit = True
        
        # 'P'인 부분만 탐색
        for i, row in enumerate(place):
            for j, x in enumerate(row):
                if x == 'P':
                    place[i] = place[i][:j] + 'O' + place[i][j+1:]
                    explore(i, j)
                    if permit == False:
                        break
            if permit == False:
                break
                
        answer.append(1 if permit == True else 0)

    return answer
