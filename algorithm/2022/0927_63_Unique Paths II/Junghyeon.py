class Solution:
    '''
    특정 인덱스에서의 경로의 수 = 위쪽의 경우의 수 + 왼쪽의 경우의 수
    '''
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # 시작지점과 도착지점에 장애물이 있으면 갈 수 있는 경로는 없다.
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        i_flag = True
        j_flag = True
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                # i == 0인 경우 장애물이 있으면 -1로 변경하고, 그렇지 않으면 1로 변경
                # 장애물이 나타난 이후에는 나머지의 열은 사용할 수 없으므로 모두 -1로 변경
                if i == 0:
                    # 이미 장애물이 한번 나타난 경우
                    if i_flag == False:
                        obstacleGrid[i][j] = -1
                        continue
                    # 장애물이 없는 경우에는 그냥 1로 변경
                    if obstacleGrid[i][j] != 1:
                        obstacleGrid[i][j] = 1
                    # 장애물이 한번 나타나면 flag값을 false로 설정해서 이후에 모든 배열을 -1로 변경
                    else:
                        obstacleGrid[i][j] = -1
                        i_flag = False
                        
                # j == 0인 경우에도 i의 경우와 마찬가지로 변경                
                elif j == 0:
                    if j_flag == False:
                        obstacleGrid[i][j] = -1
                        continue
                    if obstacleGrid[i][j] != 1:
                        obstacleGrid[i][j] = 1
                    else:
                        obstacleGrid[i][j] = -1
                        j_flag = False
                # i와 j 모두 0이 아닌곳에 장애물이 있는 경우에는 그냥 -1로 변경        
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
                    
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                # 위쪽과 왼쪽 모두 장애물이 있으면 사용할 수 없는 경로
                if obstacleGrid[i-1][j] == -1 and obstacleGrid[i][j-1] == -1:
                    continue
                    
                # 현재 지점에 장애물이 있으면 사용할 수 없는 경로
                if obstacleGrid[i][j] == -1:
                    continue
                
                # 왼쪽과 위쪽에 모두 장애물이 없으면 현재 인덱스에 두개의 값을 더해서 업데이트
                elif obstacleGrid[i-1][j] != -1 and obstacleGrid[i][j-1] != -1:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                
                # 왼쪽에 장애물이 있으면 위쪽의 값을 그대로 가져오고
                # 위쪽에 장애물이 있으면 왼쪽의 값을 그대로 가져온다.
                else:
                    if obstacleGrid[i-1][j] == -1:
                        obstacleGrid[i][j] = obstacleGrid[i][j-1]
                    elif obstacleGrid[i][j-1] == -1:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j]
        
        return obstacleGrid[-1][-1]
