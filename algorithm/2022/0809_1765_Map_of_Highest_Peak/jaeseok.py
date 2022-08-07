from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        
        # 이동할 방향 설정
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1 ,1]
        
        # output은 isWater의 배열과 크기는 똑같지만 전부 0으로 초기화된 배열부터 시작
        output = [[0 for _ in range(n)] for _ in range(m)]
        
        q = deque()
        
        # bfs 구현
        def bfs(q, output):
            while q:
                x, y = q.popleft()
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    
                    # 방문할 지점이 배열의 범위를 벗어나는지 체크
                    if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n:
                        continue
                    # 아직 방문하지 않고(즉, 아직 0인 지점) 물이 있는 지점이 아니면 height를 지정
                    if output[new_x][new_y] == 0 and not isWater[new_x][new_y]:
                        output[new_x][new_y] = output[x][y] + 1
                        # 새로운 지점을 queue에 추가
                        q.append((new_x, new_y))
            return output
        
        for i in range(m):
            for j in range(n):
                # isWater인 지점부터 queue에 담아 bfs를 수행
                if isWater[i][j] == 1:
                    q.append((i, j))
                
        output = bfs(q, output)
        return output
                    
