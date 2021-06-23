queue = deque([(0,1)])
# (현재 위치, 가야하는 방향)으로 set을 만들어줌
count = 0
# 벌레가 몇 번 움직였는지 
forbidden = set(forbidden)
# 다시 갈 수 없더나 애초에 갈 수 없는 지점을 forbidden으로 표시
forbidden.add(0)
# 처음에 0에서 시작하니 0을 forbidden에 더해준다.
        
MAX_DIST = max(x, max(forbidden)) + a + b
# 거리의 최대값을 설정해주는데 왜 forbidden을 참조하는지 의문        

while queue:
    tmp = deque()
    for elem in queue:
    # queue안에 원소가 있을 때 루프를 돌게 됨
        (pos, direction) = elem
        #이 때 현재 위치와 방향을 pos와 direction으로 받음
        if pos == x: return count
        # 현재 위치가 목적지와 같을 경우 count를 return 
        forward = pos + a
        # 현재 위치가 목적지와 같지 않을 경우 pos에 a만큼 더해줌
        if (forward not in forbidden) and (forward <= MAX_DIST):
        # 만약 forward가 forbidden안에 있지 않고 최대거리 보다 작을 경우 루프를 돔
            tmp.append((forward, 1))
            # 이 경우 벌레가 앞으로 뛴 경우이므로 tmp에 현재 위치를 갱신해주고 방향도 설정해줌
            forbidden.add(forward)
            # 현재 위치는 이미 지났으니까 forbidden에 현재 위치를 넣어줌
            
    for elem in queue:
        (pos, direction) = elem
        if pos == x: return jumps
        #이번엔 벌레가 뒤로 뛰는 경우를 가정해봄
        backward = pos - b
        if (direction != -1) and (backward >= 0) and (backward not in forbidden):
            # direction이 -1이 아닐때 뒤로 뛰는 이유는 연속해서 두 번 뒤로 갈 수 없기 때문
            tmp.append((backward, -1))
            forbidden.add(backward)
    queue = tmp
    # 루프를 모두 돌아 1번의 루프가 끝났으면 큐에 tmp값을 갱신하여 현재 위치와 방향을 알려줌
    count += 1
return -1
