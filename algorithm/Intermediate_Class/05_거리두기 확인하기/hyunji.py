from collections import deque

def bfs(place):
    p_list = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 사람이 앉은 곳('P')의 index와 distance(0)를 list에 넣어준다
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                p_list.append((i, j, 0))
    
    for p in p_list:
        # 현재 'P'의 index를 큐에 넣어줌
        queue = deque([p])  
        visited = [[0]*5 for i in range(5)]
        
        while queue:
            x, y, d = queue.popleft()
            visited[x][y] = 1
            
            # 4 방향 방문
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 한 방향으로 움직일 때마다 distance를 1씩 증가시킴
                nd = d + 1
                
                # index가 범위 밖으로 나가지 않고 아직 방문하지 않은 지점이라면
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    
                    # 'O'이고, 현재 distance가 1 이하인 경우만 더 탐색할 수 있음
                    if place[nx][ny] == 'O' and nd <= 1:
                        queue.append((nx, ny, nd))
                    
                    # distance가 2 이내인데 현재 방문한 지점이 'P'인 경우 
                    # 바로 return 0
                    if place[nx][ny] == 'P' and nd <= 2:
                        return 0
    return 1


def solution(places):
    answer = []
    
    for place in places:
        res = bfs(place)
        answer.append(res)

    return answer
