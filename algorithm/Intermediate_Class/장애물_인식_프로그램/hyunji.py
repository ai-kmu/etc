import sys
from collections import deque

N = int(input())
matrix = []
answer = []

# 행렬 input 받기
for i in range(N):
    number = list(map(int, input()))
    matrix.append(number)

# 방문 안한 경우: visited[i] = 0
# 방문 한 경우: visited[i] = 1
visited = [[0]*N for i in range(N)]


def BFS(row, col, cnt):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque()
    
    # 현재 행렬 index를 큐에 넣고 방문 처리
    q.append([row, col])
    visited[row][col] = 1

    while q:
        i, j = q.popleft()

        # 네 가지 방향에서 탐색(좌, 우, 위, 아래)
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            # 이동한 index가 행렬의 range 밖을 벗어나면 안된다.
            if nx > -1 and nx < N and ny > -1 and ny < N:
                # 이동한 index에서의 행렬 값이 1(장애물)이고, 방문한 적이 없는 경우
                if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                    # 큐에 넣어주고, 장애물 + 1 해주고, 방문 처리
                    q.append([nx, ny])
                    cnt += 1
                    visited[nx][ny] = 1

    answer.append(cnt)

    
for i in range(N):
    for j in range(N):
        # 값이 1이고, 방문하지 않은 부분만 BFS로 탐색
        if matrix[i][j] == 1 and visited[i][j] == 0:
            BFS(i, j, 1)

print(len(answer))

for i in sorted(answer):
    print(i)
