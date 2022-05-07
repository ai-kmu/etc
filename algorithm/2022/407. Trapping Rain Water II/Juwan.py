# 참고 https://conpulake.tistory.com/248

import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        y_axis = len(heightMap)
        x_axis = len(heightMap[0])
        queue = []
        
        visited = [[0]*x_axis for _ in range(y_axis)]

        
        for i in range(y_axis):
            for j in range(x_axis):
                if i == 0 or j == 0 or i == y_axis-1 or j == x_axis -1:
                    
                    heapq.heappush(queue, (heightMap[i][j], i, j))
                    visited[i][j] = 1
                    
        ans, height = 0, 0
 
        while queue:
            
            h, i, j = heapq.heappop(queue)
                        
            height = max(height, h)
            
            ans += max(height - h, 0)
            
            for a, b in ((i, j+1), (i+1, j), (i-1, j), (i, j-1)):
                if  0 <= a < y_axis and 0 <= b < x_axis and visited[a][b] != 1:
                    heapq.heappush(queue, (heightMap[a][b], a, b))
                    visited[a][b] = 1

        return ans
