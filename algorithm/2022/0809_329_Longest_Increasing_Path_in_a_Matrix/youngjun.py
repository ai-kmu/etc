# dfs 사용하여 풀이
# but 해당 정점에서 갈 수 있는 모든 점 다 탐색 ㅠㅠ case를 나누는 방법 아직 못찾음 ㅠ

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cols, rows = len(matrix[0]), len(matrix)

        answer = 1

        def dfs(c, r, n):

            direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            length = n

            for dx, dy in direct:
                nx = c + dx
                ny = r + dy

                if (nx < 0 or nx >= cols) or (ny < 0 or ny >= rows) or matrix[r][c] >= matrix[ny][nx]:
                    continue

                if matrix[r][c] < matrix[ny][nx]:
                    length = dfs(nx, ny, length + 1)

            return length

        for i in range(cols):
            for j in range(rows):
                answer = max(dfs(i, j, 1), answer)

        return answer
