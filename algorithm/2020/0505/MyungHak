from collections import deque

"""
    넓이 우선 탐색을 이용하여 풀면 된다.
    단 한쪽에서만 시작하는 넓이 우선 탐색 방법으로는 시간 초과가 나오기 때문에 
    양쪽에서(시작점, 도착점) 출발하는 넓이 우선 탐색 방법을 사용해야 한다.
"""

import copy
import queue

maximum_distance = 1000000
def solution(maps):
    answer = 0
    maxX = len(maps[0])
    maxY = len(maps)
    
    
    #우선 통로는 maximum_distance로 초기화 해준다. 그후 각각 끝점과 시작점을 1로 초기화해준다.
    #그리고 시작점으로부터의 거리를 잴 maps 와 끝점으로부터의 거리를 잴 target_maps를 선언해준다.
    maps = [[maps[i][j] *maximum_distance for j in range(maxX)]for i in range(maxY)]
    target_maps = copy.deepcopy(maps)
    target_maps[-1][-1] = 1
    maps[0][0]=1
    
    
    # 시작점과 끝점으로 부터 BFS를 시작한다
    map_Q = deque()
    map_Q.append([0,0, 1])
    target_Q = deque()
    target_Q.append([-1,-1,1])
    
    while True:
        if len(map_Q) == 0:
            return -1
        Py, Px, answer = map_Q.popleft()
        if(maximum_distance>target_maps[Py][Px]>=1): # BFS중 끝점과 시작점이 만나는 경우 둘의 합에 1을 빼 답으로 반환한다
            return answer + target_maps[Py][Px] -1

        for i in range(-1,2,2):
            if -1 < Px + i < maxX and maps[Py][Px+i] > answer + 1:
                maps[Py][Px + i] = answer+1
                map_Q.append([Py,Px+i, answer+1])
            if -1 < Py + i < maxY and maps[Py+i][Px] > answer + 1:
                maps[Py + i][Px] = answer+1
                map_Q.append([Py+i,Px, answer+1])
#####################################여기서부터는 도착점으로 부터 시작하는 BFS######################################
        if len(target_Q) == 0:
            return -1
        Ty, Tx, dist = target_Q.popleft()
        if(maximum_distance>maps[Ty][Tx]>=1): # BFS중 끝점과 시작점이 만나는 경우 둘의 합에 1을 빼 답으로 반환한다
            return dist + maps[Ty][Tx] - 1
        
        for i in range(-1,2,2):
            if -maxX<=Tx + i < 0 and target_maps[Ty][Tx+i] > dist+1:
                target_maps[Ty][Tx+i] = dist+1
                target_Q.append([Ty,Tx+i,dist+1])
            if -maxY<=Ty + i < 0 and target_maps[Ty+i][Tx] > dist+1:
                target_maps[Ty+i][Tx] = dist+1
                target_Q.append([Ty+i,Tx, dist+1])

    return answer
