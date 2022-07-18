from collections import deque
import sys

N = int(input())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().strip()))

# bfs를 위한 deque
Q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 결과 저장을 위한 리스트
res = []
# 현재 몇개의 장애물이 있는지 세는 변수
cnt = 0

for i in range(N):
    for j in range(N):
        # 현재 위치가 1일 때만 탐색 시작
        if board[i][j] == '1':
            Q.append((i, j))
            board[i][j] = '0'
            cnt += 1
            # bfs 진행
            while Q:
                x, y = Q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '1':
                        Q.append((nx, ny))
                        board[nx][ny] = '0'
                        cnt += 1
            # dfs가 끝난 후 cnt를 res에 저장
            # 이후 cnt 0으로 초기화
            if cnt != 0:
                res.append(cnt)
                cnt = 0

res.sort()
print(len(res))

for i in res:
    print(i)
