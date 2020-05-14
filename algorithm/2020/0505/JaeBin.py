# 19. 프로그래머스 - 게임 맵 최단거리

def solution(maps):
    # 상대 팀 진영에 도착할 수 없을 경우
    answer = -1

    # 게임 맵의 크기
    game_map_size = len(maps) - 1
    # 맵의 크기(사용자)
    map_size = len(maps[0]) - 1

    # 이동방향
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 경로 저장 리스트
    path_lst = []

    # 게임 시작 위치, 1부터 시작
    path_lst.append([0, 0, 1])

    while path_lst:
        # 현재 위치
        x, y, cnt = path_lst.pop(0)
        # 지나온 길 벽으로 없애기
        maps[x][y] = 0
        # 너비 우선 탐색, 상하좌우
        for dx, dy in directions:
            mx, my = x + dx, y + dy
            # 마지막 지점 먼저 도달하면 경로 출력
            if mx == game_map_size and my == map_size:
                answer = cnt + 1
                return answer
            if 0 <= mx <= game_map_size and 0 <= my <= map_size and maps[mx][my] == 1:
                maps[mx][my] = 0
                path_lst.append([mx, my, cnt+1])
    return answer

maps_1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps_2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

print(solution(maps_1))
print()
print(solution(maps_2))