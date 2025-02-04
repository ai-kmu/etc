class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        
        rows = [i for i, x in enumerate(rows) if x == 1]
        cols = [i for i, x in enumerate(cols) if x == 1]

        answer = 0
        for row in rows:
            for col in cols:
                if mat[row][col] == 1:
                    answer += 1
        return answer
