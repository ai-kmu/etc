class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        # 현재 위치의 값을 사용 가능한지 확인하는 함수
        not_available = lambda i, j: not(0 <= i < m and 0 <= j < n and matrix[i][j] is not None)

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        count = 0
        dir_index = 0
        row, col = 0, 0
        answer = [None] * (m * n)

        while count < m * n:
            answer[count] = matrix[row][col]
            matrix[row][col] = None
            new_row = row + dirs[dir_index][0]
            new_col = col + dirs[dir_index][1]

            # 만약 사용 불가능하면 방향을 바꿈
            if not_available(new_row, new_col):
                dir_index = (dir_index + 1) % 4
                new_row = row + dirs[dir_index][0]
                new_col = col + dirs[dir_index][1]
            row = new_row
            col = new_col
            count += 1
        return answer
