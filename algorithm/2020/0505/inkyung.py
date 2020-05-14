from collections import deque

def BFS(start, graph):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]     #갈 수 있는 방향
    queue = deque([start])
    
    while queue:
        y, x, cnt = queue.popleft()
        graph[y][x] = 0
        for dir_y, dir_x in directions:
            new_y, new_x = y + dir_y, x + dir_x
            
            #만약 이동한 위치가 상대팀 진형이라면 cnt + 1 리턴
            if new_y == len(graph) - 1 and new_x == len(graph[0]) - 1:
                return cnt + 1
            
            #만약 x, y가 map안에 위치하면서 해당 위치 값이 1이라면
            #이미 지나온 값으로 쌓아버리고 좌표값을 0으로 바꿔버리면 다시 못돌아감
            elif 0 <= new_y < len(graph) and 0 <= new_x < len(graph[0]) and graph[new_y][new_x] == 1:
                graph[new_y][new_x] = 0
                queue.append((new_y, new_x, cnt + 1))
    #해결안된 모든 경우는 -1 리턴
    return -1
                
def solution(maps):
    return BFS((0, 0, 1), maps)
