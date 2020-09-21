class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
            2차원 행렬의 경우 reverse 후에 transpose하면 시계방향으로 90도 회전하는 in-place 알고리즘이 됨
        """
        matrix.reverse()
        for i in range(0,len(matrix)):
            for j in range(1,len(matrix[i])-i):
                matrix[i][i+j], matrix[i+j][i] = matrix[i+j][i], matrix[i][i+j] #transpose
        
