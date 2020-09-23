class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        # Transpose 
        for i in range(n):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        # 좌우 반전하기
        for i in range(n):
            for j in range(n//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j] # 현재 위치 값과 반대 위치값이랑 바꿔주기
                matrix[i][n - 1- j] = tmp
