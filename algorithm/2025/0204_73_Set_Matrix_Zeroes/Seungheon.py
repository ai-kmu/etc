class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # 변환 함수
        def change_to_zero(m, n):
            row_num = len(matrix)
            col_num = len(matrix[0])
            for i in range(row_num):
                matrix[i][n] = 0
            for i in range(col_num):
                matrix[m][i] = 0
        
        # 변환 할 위치 찾기
        zero_set = set() 
        for row_idx, row  in enumerate(matrix):
            for col_idx, value in enumerate(row):
                if value == 0:
                    zero_set.add((row_idx, col_idx))
        # 찾은 위치 변환
        for m, n in zero_set:
            change_to_zero(m, n)

        return matrix
