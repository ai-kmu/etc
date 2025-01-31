class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()
        
        # 0이 되어야하는 행, 열 탐색
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        # row -> zero
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0
        
        # columns -> zero
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0
        
        return matrix
