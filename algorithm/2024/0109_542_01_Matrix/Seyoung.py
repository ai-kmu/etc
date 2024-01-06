from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque() #BFS에 쓰일 큐
        distance = [[float('inf')] * cols for _ in range(rows)]
        
        # 셀이 0 이면 큐에 추가
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    distance[i][j] = 0
        
        # BFS를 이용해 최단 거리 구하기
        while queue:
          # 현재 위치
            curr_x, curr_y = queue.popleft()
          # 현재위치에서 움직여서 새로운 위치로 감
            for dx, dy in directions:
                new_x, new_y = curr_x + dx, curr_y + dy 
               # 새로운 위치가 행렬 범위 내에 있는지 확인  후 거리계산
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    new_distance = distance[curr_x][curr_y] + 1 
                  # 최단 거리면 큐에 추가
                    if new_distance < distance[new_x][new_y]:
                        distance[new_x][new_y] = new_distance
                        queue.append((new_x, new_y))
        return distance
