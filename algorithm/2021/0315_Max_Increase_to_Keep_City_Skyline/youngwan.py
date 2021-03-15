class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_tb = [0 for i in range(len(grid[0]))]                      # top, bottom의 skyline 
        max_lr = [0 for i in range(len(grid))]                         # left, right의 skyline
        
        for i in range(len(grid[0])):                                  # 각 grid 마다
            for j in range(len(grid)):
                if grid[i][j] > max_tb[i]:                             # top, bottom의 가장 큰 skyline 값 저장
                    max_tb[i] = grid[i][j]
                if grid[i][j] > max_lr[j]:                             # left, right의 가장 큰 skyline 값 저장
                    max_lr[j] = grid[i][j]
                    
        sum = 0
        
        for i in range(len(grid[0])):                                  # 각 gird 마다
            for j in range(len(grid)):
                before = grid[i][j]                                
                if max_tb[i] < max_lr[j]:                              # top, bottom과 left, right의 skyline 값 중 작은 값과 이전 값과의 차이를 저장
                    sum += (max_tb[i] - before)
                else:
                    sum += (max_lr[j] - before)
        
        return sum
