# 구현을 제대로 못해서 아예 오답코드 입니다.
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        
        # 이동할 방향
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = deque()
        
        # bfs 구현
        def bfs(x,y):
            while queue:
                x, y = queue.popleft()
                # 4방향 확인
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 공간 벗어나면 무시
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    # 방문하지 않고 물이 없는곳을 업데이트
                    if graph[nx][ny] == 0 and not isWater[nx][ny]:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
            return graph
        # 이제 그래프 생성하고 넣어서 하면 될거 같은데..
