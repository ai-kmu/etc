from collections import deque
class Solution:
    def highestPeak(self, isWater):
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
        # map 만들기
        water_map = [ [float('inf') for _ in range(len(isWater[0])) ]  for _ in range(len(isWater))]
        
        # Q에 물이있는지점 append
        Q = deque()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    Q.append([i, j, 0])
        
        # BFS
        while Q:
            cur_i, cur_j, point = Q.popleft()
            
            # 범위 밖
            if cur_i < 0 or cur_j < 0 or cur_i >= len(isWater) or cur_j >= len(isWater[0]):
                continue
            
            # 더 작은수가 있으면 작은 수 사용
            if water_map[cur_i][cur_j] <= point:
                continue
            
            # map 에 point 입력 
            water_map[cur_i][cur_j] = point

            for dy, dx in directions:
                Q.append([cur_i + dy, cur_j + dx, point + 1])
 
        return water_map
