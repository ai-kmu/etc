from typing import List


class Solution :
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # m x n 사각형, n개 공
        # 공이 V자에 걸리면 실패
        # 양 사이드 벽에 닿으면 실패
    
        # m : grid 길이 
        m = len(grid)
        # n : grid의 0번 index 개수
        n = len(grid[0])

        def is_canfall(i,j):
            if i == m:
                return j

            # 오른쪽 끝에서 정방향으로 떨어져서 벽에 닿음
            elif j == n-1 and grid[i][j] == 1:
                return -1
            # 왼쪽 끝에서 역방향으로 떨어져서 벽에 닿음
            elif j == 0 and grid[i][j] == -1:
                return -1

            # V자에 걸렸는데, 왼쪽 공 stuck
            elif grid[i][j] == 1 and grid[i][j+1] == -1:
                return -1

            # V자에 걸렸는데, 오른쪽 공 stuck
            elif grid[i][j] == -1 and grid[i][j-1] == 1:
                return -1

            return is_canfall(i+1,j+grid[i][j])
        
        return [is_canfall(0,j) for j in range(n)]    

grid1 = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
grid2 = [[-1]]
grid3 = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
a = Solution()
print("output :", a.findBall(grid1))
