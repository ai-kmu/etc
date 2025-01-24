class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        zero_point = []
        # 돌면서 0인 포인트 찾기
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_point.append((i, j))
                

        # 찾은 포인트의 열과 행을 0으로 
        for row, col in zero_point:
            for j in range(m):
                matrix[row][j] = 0
            for i in range(n):
                matrix[i][col] = 0
        return matrix
