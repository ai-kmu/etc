from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        rows = len(isWater)
        cols = len(isWater[0])
        visited = [[0] * cols for _ in range(rows)]
        q = deque()
        
        # isWater 값을 모두 0으로 초기화
        # 물웅덩이 부분은 q에 넣고 visited 처리
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    visited[i][j] = 1
                    q.append((i, j))
                                
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        height = 0
        
        while q:
            xx, yy = q.popleft()
            # 4방향으로 탐색(동서남북)
            for i in range(4):
                nx = xx + dx[i]
                ny = yy + dy[i]
                
                # 새로 방문한 지점이 index를 벗어나지 않고, 아직 방문하지 않은 곳이면
                if nx >= 0 and ny >= 0 and nx < rows and ny < cols and visited[nx][ny] == 0:
                    # 방문처리
                    visited[nx][ny] = 1
                    # 큐에 넣기
                    q.append((nx, ny))
                    # height를 1만큼 더해준다
                    isWater[nx][ny] = isWater[xx][yy] + 1
            
        return isWater
                
            
