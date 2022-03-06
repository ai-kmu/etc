import numpy as np

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # numpy의 matrix를 사용해서 int타입으로 변경
        matrix = np.matrix(matrix).astype(np.int)
        col, row = matrix.shape[0], matrix.shape[1]
        
        # 근처 값들이 모두 1인 경우를 찾고, 만약 있다면 값을 업데이트
        for i in range(col-2, -1, -1):
            for j in range(row-2, -1, -1):
                if matrix[i, j] == 1:
                    matrix[i, j] = min(matrix[i+1, j], matrix[i, j+1], matrix[i+1, j+1]) + 1
        
        # 가장 큰 값을 가진 경우가 주변에서 1이 가장 많은 것을 의미 -> 그만큼의 면적을 가지면 되므로 제곱
        return matrix.max() ** 2
