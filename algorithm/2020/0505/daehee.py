import collections

def solution(maps):
    def check(pair):                        # 갈 수 있는 위치인지 확인해주는 함수
        x, y = pair
        if x < 0 or y < 0:
            return False
        try:
            if maps[y][x] == 1:
                return True
        except:
            return False
        return False
        
    x_len = len(maps[0])                    # x,y 최댓값
    y_len = len(maps)
    target = (x_len-1, y_len-1)             # target 좌표
    first = (0,0)                           # 시작 좌표
    deq = collections.deque()
    deq.append(first)                       # 시작 좌표 삽입
    answer = 0
    
    while len(deq) > 0:                     # BFS 끝날때까지 돌기
        x, y = deq.popleft()
        answer = maps[y][x]                 # 현재 값이 BFS depth
        # for a in maps:
        #     print(a)
        # print("==========================")
        if (x, y) == target:                # 현재 좌표가 target이면 리턴
            return answer
        
        left = (x-1, y)
        up = (x, y-1)
        right = (x+1, y)
        down = (x, y+1)

        if check(left):                      # 각 방향 확인
            maps[y][x-1] = answer+1          # maps를 지금보다 +1 해줌(depth 갱신)
            deq.append(left)                 # 갈 수 있는 좌표 삽입
        if check(right):
            maps[y][x+1] = answer+1
            deq.append(right)
        if check(up):
            maps[y-1][x] = answer+1
            deq.append(up)
        if check(down):
            maps[y+1][x] = answer+1
            deq.append(down)
    return -1
