from collections import deque

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # 예외처리
        if obstacleGrid[-1][-1] == 1:
            return 0
        
        # obstacle이 양수로 되어있어서 경로를 음수로 더한 후 마지막에 -를 취함
        answer = 0        
        Q = deque([[0, 0]])
        
        while Q:

            cur_i, cur_j = Q.popleft()
            
            # 방문처리
            try:
                if obstacleGrid[cur_i][cur_j] < 0 or obstacleGrid[cur_i][cur_j] == 1:
                    continue
            except:
                continue
            
            # obstacle이 있는곳과 범위 밖은 0 아닌곳은 경로의 수
            try:
                up = 0 if obstacleGrid[cur_i-1][cur_j] == 1 else obstacleGrid[cur_i-1][cur_j]
            except:
                up = 0
            try:
                left = 0 if obstacleGrid[cur_i][cur_j-1] == 1 else obstacleGrid[cur_i][cur_j-1]
            except:
                left = 0
                
            obstacleGrid[cur_i][cur_j] = up + left + (-1 if [cur_i, cur_j] == [0,0] else 0)
            
            # 탐색
            for dy, dx in [[1,0],[0,1]]:
                Q.append([cur_i + dy, cur_j + dx])

        
        return -obstacleGrid[-1][-1]
