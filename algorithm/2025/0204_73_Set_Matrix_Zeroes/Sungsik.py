class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(mn)으로 풀어야함
        m, n = len(matrix), len(matrix[0])
        rows, cols = [False] * m, [False] * n

        # 바꿀 위치를 저장
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        # 저장한 row와 col을 0으로 설정
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
