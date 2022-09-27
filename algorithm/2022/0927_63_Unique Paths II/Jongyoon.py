from collections import deque
"""
시간 초과
"""
class Solution(object):
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dx = [1, 0]                                 # 아래로 이동
        dy = [0, 1]                                 # 오른쪽으로 이동
        
        result = 0                                  # 경로의 수 초기화
        queue = deque()
        queue.append((0, 0))                        
        
        if obstacleGrid[0][0] == 1:                 # 출발부터 장애물이 있으면 -> 경로가 없음
            return 0
            
        while queue:
            x, y = queue.popleft() 
            
            if m == 1 and n == 1:                   # 입구 = 출구 -> 경로가 1개
                if obstacleGrid[x][y] == 0:         
                    return 1
                else:
                    return 0
            
            for i in range(2):                      
                nx = x + dx[i]
                ny = y + dy[i]
 
                if nx >= m or ny >= n :              # grid를 벗어나는 경우
                    continue
                
                if obstacleGrid[nx][ny] == 1:        # 장애물이 있는 경우
                    continue
                    
                if obstacleGrid[nx][ny] == 0:        # 장애물이 없는 경우
                    if nx == m - 1 and ny == n - 1:  # 출구까지 도달하게 되면
                        result += 1                  # 값을 count한다.
                    queue.append((nx, ny))
                    
        return result
                   
