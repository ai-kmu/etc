class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        row = len(grid)
        col = len(grid[0])
        answer = [-1] * col
                    
        for ball in range(col):
            i = 0
            j = ball
            
            while i < row:
                # 왼쪽 끝의 위치에서 -1 방향으로 떨어지면 벽에 부딪히면서 stuck
                if j == 0 and grid[i][j] == -1:
                    break
                
                # 오른쪽 끝의 위치에서 1 방향으로 떨어지면 벽에 부딪히면서 stuck 된다
                elif j == col-1 and grid[i][j] == 1:
                    break
                    
                # 'V' shape 모양에서 걸렸을 때 왼쪽 공이 stuck 상태가 됨
                elif grid[i][j] == 1 and grid[i][j+1] == -1:
                    break
                
                # 'V' shape 모양에서 걸렸을 때 오른쪽 공이 stuck 상태가 된다
                elif grid[i][j] == -1 and grid[i][j-1] == 1:
                    break
                
                # stuck 되지 않은 경우
                else: 
                    # 현재 방향이 1인 경우
                    if grid[i][j] == 1:
                        i += 1
                        j += 1
                
                    # 현재 방향이 -1인 경우
                    else:
                        i += 1
                        j -= 1
            
            if i == row:
                answer[ball] = j
                
        return answer
