class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    for k in range(col):
                        if matrix[i][k] == 0: 
                            continue
                        matrix[i][k] = 'a'
                    for k in range(row):
                        if matrix[k][j] == 0: 
                            continue
                        matrix[k][j] = 'a'
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
