class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 행, 열 탐색용 set 선언 및 길이 저장
        rows, cols = set(), set()
        len_r = len(matrix)
        len_c = len(matrix[0])

        # 0인 행, 열 탐색
        for i in range(len_r):
            for j in range(len_c):
                if not matrix[i][j]:
                    rows.add(i)
                    cols.add(j)

        # 0이 들어있는 행 전부 0으로 변환
        for r in rows:
            for c in range(len_c):
                matrix[r][c] = 0

        # 0이 들어있는 열 전부 0으로 변환
        for c in cols:
            for r in range(len_r):
                matrix[r][c] = 0
