# bfs로 풀이
# 해당 경로에 갈수 있는 가짓수를 구합니다
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        move = [(0, -1), (-1, 0)] # 이동경로, 오른쪽이나 밑으로밖에 못간다는 문제의 가정
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1: # 시작이 끝인경우 이동할필요가없음
            return 0
        
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0: # 시작점에 대한 예외처리만
                    obstacleGrid[0][0] = 1
                    continue
                
                # 장애물이 확인됬을때 지나갈수 없으므로 0으로 처리하고 무시
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                
                # bfs
                for m in move:
                    next_row = i + m[0]
                    next_col = j + m[1]
                    if next_row < 0 or next_col < 0 or row <= next_row or col <= next_col:
                        continue
                    obstacleGrid[i][j] += obstacleGrid[next_row][next_col]
        
        return obstacleGrid[row-1][col-1]

