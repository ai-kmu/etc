class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set()
        len_r = len(matrix)
        len_c = len(matrix[0])

        for i in range(len_r):
            for j in range(len_c):
                if not matrix[i][j]:
                    rows.add(i)
                    cols.add(j)

        for r in rows:
            for c in range(len_c):
                matrix[r][c] = 0
        
        for c in cols:
            for r in range(len_r):
                matrix[r][c] = 0
