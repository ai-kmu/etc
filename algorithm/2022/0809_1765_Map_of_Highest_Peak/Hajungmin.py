from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dq = deque()
        row, col = len(isWater), len(isWater[0])
        d = [(0,1),(1,0),(0,-1),(-1,0)]
        
        # 이중 루프를 돌며 만약 1일 경우 BFS를 수행하기 위해 좌표를 dq에 넣는다.
        # 그리고 방문 처리를 해주고 만약 1이 아닐경우 큰 수로 정의한다.
        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    dq.append((i,j))
                    isWater[i][j] = 0 
                else:
                    isWater[i][j] = 9999
    
        # BFS를 수행하며 9999일 경우에만 탐색하기 시작해서 방문하는 곳들을 1씩 더해준다
        while dq:
            x, y = dq.popleft()
            
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
            
                if 0 <= nx < row and 0 <= ny < col and isWater[nx][ny] == 9999:
                    isWater[nx][ny] = isWater[x][y]+1
                    dq.append((nx, ny))
                    
        return isWater
