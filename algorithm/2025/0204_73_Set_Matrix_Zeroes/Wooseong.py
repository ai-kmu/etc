class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 크기 측정
        m = len(matrix)
        n = len(matrix[0])

        # 0이 있는 column 체크를 위한 리스트
        zero_cols = [False for _ in range(n)]

        # row를 0으로 만들기
        for row in matrix:
            # row에 0이 있다면
            if 0 in row:
                # 그 줄 전체 0으로 만들기
                for i, r in enumerate(row):
                    # 0인 column 체크
                    if r == 0:
                        zero_cols[i] = True
                    row[i] = 0

        # column을 0으로 만들기
        for i, zero in enumerate(zero_cols):
            if zero:
                for r in range(m):
                    matrix[r][i] = 0
