# 1st approach
# 1인 부분을 시작지점으로 잡으려고 하니 큐에 너무 많이 담아야 함
# memory limit

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        answer = [[0] * n for _ in range(m)]
        
        q = deque()
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    q.append((1, i, j, i, j))
        
        while q:
            dist, x, y, ox, oy = q.popleft()
            if answer[ox][oy] != 0:
                continue
            for i, j in zip(dx, dy):
                nx = x + i
                ny = y + j
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if mat[nx][ny] == 0:
                    answer[ox][oy] = dist
                    break
                else:
                    q.append((dist + 1, nx, ny, ox, oy))
                    
        return answer

# 2nd approach
# 0을 기준으로 탐색

from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        q = deque()
        # 이동할 방향 설정
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        # length의 최대 길이는 10000을 넘길 수 없으므로 mat가 1인 부분은 10000으로 초기화
        # mat가 0인 부분을 시작지점으로 삼을 것이므로 deque에 추가
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = 10000
                else:
                    q.append((1, i, j))

        # BFS
        # 0을 기준으로 상하좌우를 탐색, mat의 범위를 벗어나는 곳은 제외
        # 0에서 각각의 1까지의 최단거리를 계속 갱신
        while q:
            dist, x, y = q.popleft()
            for i, j in zip(dx, dy):
                nx = x + i
                ny = y + j
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if mat[nx][ny] != 0 and dist < mat[nx][ny]:
                    mat[nx][ny] = dist
                    q.append((dist + 1, nx, ny))
