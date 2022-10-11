from collections import deque
def solution(maps):
    
    # 4가지 방향 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # row, column
    r = len(maps)
    c = len(maps[0])

    # 방문 표시 + 현재까지 지나온 칸의 수를 기록하는 별도의 맵
    graph = [[-1 for _ in range(c)] for _ in range(r)]

    # 데크에 현재 위치 넣어주기
    queue = deque()
    queue.append([0, 0])

    # 처음 위치 방문처리 + 첫 번째 위치여서 1
    graph[0][0] = 1

    # 큐를 돌며 BFS 수행
    while queue:
        y, x = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 밖을 나가지 않고 벽이 아닌 조건이고 현재 방문 하지 않은 위치일 때
            # 별도의 맵에서도 방문하지 않았으면 현재 값에 1을 더해서 다음 칸 갱신
            # 다음 탐색할 위치 큐에 넣기
            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] != 0:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])
                    
    # 별도의 맵의 마지막 값 출력
    answer = graph[-1][-1]
    return answer
