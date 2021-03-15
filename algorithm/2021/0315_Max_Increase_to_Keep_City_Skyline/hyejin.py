class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # max 찾기
        column_max = []
        row_max = []
        grid_size = len(grid)
        
        # column view와 row view에서 max값 찾기
        for r in range(grid_size):
            r_max = max(grid[r])
            row_max.append(r_max)
            c_max = grid[0][r]
            for c in range(grid_size):
                c_max = max(c_max, grid[c][r])
            column_max.append(c_max)
        
        # total sum
        sum = 0
        # row 순서대로 각 element를 max height로 설정하고 difference 더해주기
        for i in range(grid_size):
            for j in range(grid_size):
                if column_max[j] > row_max[i]:
                    sum += row_max[i] - grid[i][j]
                else:
                    sum += column_max[j] - grid[i][j]
        
        return sum
