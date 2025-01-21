class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 참조를 위한 matrix 생성
        tmp = deepcopy(matrix)

        # 행 안에 0이 있으면 그 행은 전부 0으로 변경
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                matrix[i] = [0] * len(matrix[i])

        # 열 안에 0이 있으면 그 열은 전부 0으로 변경
        for i in range(len(matrix[0])):
            if 0 in [m[i] for m in tmp]:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
