class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_copy = copy.deepcopy(matrix)           # 행렬 복사
        n = len(matrix)                            
        for i in range(n):
            for j in range(n):
                matrix[i][n-1-j] = matrix_copy[j][i]  # 각 행은 새로운 행렬의 열이 되어야 하고, 각 행의 index는 새로운 열에서 역순이 된다.
