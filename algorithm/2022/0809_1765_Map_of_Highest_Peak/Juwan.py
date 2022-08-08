from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        m = len(isWater) # 세로 길이
        n = len(isWater[0]) # 가로 길이
        
        to_visit = deque([]) # 이 문제는 BFS로 풀어야함
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1: # 만약 물이면, BFS 방문해야할 것에 추가
                    to_visit.append([i,j])
                    isWater[i][j] = 0
                else:
                    isWater[i][j] = -1 # 그게 아니면 0
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        
        while to_visit:
            
            x, y = to_visit.popleft()
            
            for i, j in zip(dx, dy): # zip으로 묶어서 한번에 수행
                
                if (x+i >= 0 and x+i <= m-1) and (y+j >= 0 and y+j <= n-1) and isWater[x+i][y+j] == -1: # 각 조건을 만족( matrix를 벗어나지 않으면서 탐색하지 않은 곳 )
                    isWater[x+i][y+j] = isWater[x][y] + 1 # 이전의 값을 추가
                    to_visit.append([x+i, y+j]) # 다음을 방문
        return isWater
                
            
            
