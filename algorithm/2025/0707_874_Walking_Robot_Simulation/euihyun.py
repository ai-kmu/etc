# 뭔가 풀만했는데 하다가 막혔수;; 리뷰 안해주셔도 됩니다

def robotSim(commands, obstacles):
    # 동서남북 이동
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 현재 위치 및 방향 초기화
    x = y = 0
    direction = 0  

    # 장애물을 set에 넣음
    obstacle_set = set(map(tuple, obstacles))

    max_distance_sq = 0

    # 순차적으로 처리
    for cmd in commands:
        if cmd == -2:
            # 왼쪽으로 90도 
            direction = (direction - 1) % 4
        elif cmd == -1:
            # 오른쪽으로 90도 
            direction = (direction + 1) % 4
        else:
            # cmd가 1~9일 경우 한칸씩 이동
            for _ in range(cmd):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 장애물이 없다면 이동
                if (nx, ny) not in obstacle_set:
                    x, y = nx, ny
                    # 이동 후 거리 제곱 계산 및 최대값 업데이트
                    max_distance_sq = max(max_distance_sq, x*x + y*y)
                else:
                    # 장애물이 있으면 이동 멈춤
                    break

    return max_distance_sq
