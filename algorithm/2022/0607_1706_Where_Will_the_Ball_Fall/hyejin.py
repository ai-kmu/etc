class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # m x n box, n개의 ball / 
        # top left - bottom-right => 1
        # top right - bottom-left => -1
        # 공이 v에 걸리거나, 양쪽 벽에 닿으면 실패
        # 어느 컬럼에 안착했는지, -1은 box에 갖힌 것임
        m, n = len(grid), len(grid[0])
        if n < 2:
            return [-1]
        
        # -1로 초기화, 벽쪽 padding => n+2, 도착지 => m+1
        answer = [[-1 for _ in range(n+2)] for _ in range(m+1)]
        
        # 마지막 행은 도착지 idx
        for c in range(n):
            answer[m][c+1] = c
            
        # (c-1, c) and (c와 c+1)을 pair로 봐서 all -1일 때는 answer[r][c] = answer[r+1][c-1]
        # c가 0과 n-1일 때는 벽쪽 보고 있음 -1 각자
        # all 1일 때는 answer[r][c] = answer[r+1][c+1]
        # 1, -1일 때는 answer[r][c] = -1
        for r in range(m-1, -1, -1):
            for c in range(1, n+1):
                if c < n and grid[r][c-1] == 1 and grid[r][c] == 1:
                    answer[r][c] = answer[r+1][c+1]
                elif c > 1 and grid[r][c-2] == -1 and grid[r][c-1] == -1:
                    answer[r][c] = answer[r+1][c-1]
                else:
                    answer[r][c] = -1
                    
        return answer[0][1:n+1]
