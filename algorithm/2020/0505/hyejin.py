from collections import deque


def solution(maps):
    # 방문한 횟수를 저장할 list
    visit = [[0 for _ in maps[0] ] for _ in maps]
    # bfs를 사용하기 위한 deque
    queue = deque()
    # 처음 지점을 넣어줌
    queue.append([0,0])
    # 4방향
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    
    # 처음 지점은 이미 방문
    visit[0][0] = 1
    # queue가 없을 때까지
    while queue:
        # queue에서 한개 꺼냄. 현재 x와 y => x는 row, y는 col이다.
        curr_x, curr_y = queue.popleft()
        
        # 4방향으로 다 시도
        for dir_i in directions:
            # 다음 위치
            next_x, next_y = [curr_x+dir_i[0], curr_y+dir_i[1]]
            
            # 만약 map을 벗어날 경우는 pass
            if next_x < 0 or next_y < 0 or next_x >= len(maps) or next_y >=len(maps[0]):
                continue
            # 처음 방문하고 길이 있을 경우, 현재 위치 거리 +1 저장
            if visit[next_x][next_y] == 0 and maps[next_x][next_y] == 1:
                visit[next_x][next_y] = visit[curr_x][curr_y] + 1
                queue.append([next_x, next_y])
            # 저장되어 있는 visit 거리보다 현재 위치에서 +1 한 거리가 더 적을 때
            elif visit[curr_x][curr_y] + 1 < visit[next_x][next_y] and maps[next_x][next_y] == 1:
                visit[next_x][next_y] = visit[curr_x][curr_y] + 1
                queue.append([next_x, next_y])

    # 답은 마지막 position의 거리
    answer = visit[len(maps)-1][len(maps[0])-1]
    
    # answer가 0일때는 방문하지도 않았단 뜻
    if answer == 0:
        answer = -1
    return answer
