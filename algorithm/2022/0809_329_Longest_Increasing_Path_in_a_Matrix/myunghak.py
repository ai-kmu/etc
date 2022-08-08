# 시작점이 물이 있는 위치인 넓이 우선 탐색 알고리즘


# 대부분의 경우 일반 list보다 deque가 빠릅니다.
from collections import deque 

WATER = 1

class Solution:
    def highestPeak(self, isWater):
        queue = deque([])
        
        #  지면의 높이를 저장할 리스트 제작.
        level = [[-1] * len(isWater[0]) for _ in range(len(isWater))]
        
        # 일단 물이 어디있는지를 탐색
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == WATER:
                    queue.append((i,j))
                    level[i][j] = 0
                    
                    
        while(queue):
            i,j = queue.popleft()
            
            # 4방향을 보며 범위 밖으로 나가지 않았으면서 아직 다른 값으로 채워지지 않았으면 채우기
            if 0 <= i-1 and level[i-1][j] == -1:
                level[i-1][j] = level[i][j] + 1
                queue.append((i-1, j))
                
            if i+1 < len(level) and level[i+1][j] == -1:
                level[i+1][j] = level[i][j] + 1
                queue.append((i+1, j))
                
            if 0 <= j-1 and level[i][j-1] == -1:
                level[i][j-1] = level[i][j] + 1
                queue.append((i, j-1))
                
            if j+1 < len(level[0]) and level[i][j+1] == -1:
                level[i][j+1] = level[i][j] + 1
                queue.append((i, j+1))
               
        return level
