class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        left_view = list(zip(*grid[::-1]))                                  # left view list 생성
        
        rows_max = [max(i) for i in grid]                                   # 각 view에서 max값 구하기 (skyline)
        cols_max = [max(i) for i in left_view]#[::-1]
        gridNew = [[0 for i in range(len(grid))] for j in range(len(grid))] # 새로만들 grid 생성

        summation1 = 0
        summation2 = 0
        for i in range(len(grid)):                                          # row, col max값 비교하여 작은것 새로운 grid에 입력
            for j in range(len(grid)):
                gridNew[i][j] = min(rows_max[i],cols_max[j])
                summation1 += grid[i][j]
                summation2 += gridNew[i][j]
        return summation2-summation1
