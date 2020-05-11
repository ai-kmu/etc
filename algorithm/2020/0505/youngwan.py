from collections import deque 


def solution(maps):
    short = deque([1])                             # 거리 저장
    loc_list = deque([(0,0)])                      # 위치 저장
    end = (len(maps)-1, len(maps[0])-1)            # 목적지 
    can_move = [(0,1), (1,0), (0,-1), (-1,0)]      # 움직일 수 있는 방향
    maps[0][0] = 0                                 # 시작 위치를 0으로 바꾼다
    finish = False                                 
    while not finish:                              # 성공이 될 때까지
        loc_list, short, end, can_move, maps, finish = move( loc_list, short, end, can_move, maps, finish)   # 다음 위치를 찾는 함수 실행
        if not loc_list:                           # 다음 위치로 갈 곳이 없다면 진행 불가
            break 
    if finish:                                     # 성공이 됐다면
        return short.pop()                         # 맨 마지막으로 저장된 거리를 반환 ( 목적지에 도착하면 위의 while문이 끝나기 때문에 )
    else:                                          # 성공하지 못했디면 
        return -1                                  # -1 반환


def move(loc_list, short, end, can_move, maps, finish):  # 다음 위치를 찾는 함수
    now = loc_list.popleft()                             # 현재 위치 가져오기
    dist = short.popleft()                               # 현재까지 거리 가져오기
    for i in can_move:                                   # 움직일 수 있는 방향마다
        next_loc = (now[0]+i[0], now[1]+i[1])            # 다음 위치로 움직이고
        if next_loc == end:                              # 목적지와 같다면
            finish = True                                # finish를 True로 하고
            short.append(dist+1)                         # 거리를 저장하고
            return loc_list, short, end, can_move, maps, finish  # 함수 종료
        # 다음 위치가 맵 안에 있고 1이라면
        elif -1 < next_loc[0] and next_loc[0] <= end[0] and -1 < next_loc[1] and next_loc[1] <= end[1] and maps[next_loc[0]][next_loc[1]] == 1:
            loc_list.append(next_loc)                    # 위치를 저장하고
            short.append(dist+1)                         # 거리를 1 올려 저장하고
            maps[next_loc[0]][next_loc[1]] = 0           # 현재 위치를 0으로 바꾸고
    return loc_list, short, end, can_move, maps, finish  # 함수 종료
