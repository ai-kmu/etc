class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        dir_index = 0
        row, col = 0, 0
        answer = [None] * (m * n)

        for count in range(m * n):
            answer[count] = matrix[row][col]
            # visit 처리
            matrix[row][col] = None
            new_row = row + dirs[dir_index][0]
            new_col = col + dirs[dir_index][1]

            # 새로운 위치가 index를 벗어낫거나, 이미 visit한 위치라면 방향을 바꿈
            if not(0 <= new_row < m and 0 <= new_col < n and matrix[new_row][new_col] is not None):
                dir_index = (dir_index + 1) % 4
                new_row = row + dirs[dir_index][0]
                new_col = col + dirs[dir_index][1]
            row = new_row
            col = new_col
        return answer
