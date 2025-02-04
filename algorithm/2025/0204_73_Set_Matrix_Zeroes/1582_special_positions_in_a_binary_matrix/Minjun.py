class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        col = [0 for i in range(len(mat[0]))]
        row = [0 for i in range(len(mat))]

        for i, r in enumerate(mat):
            for j, x in enumerate(r):
                if x == 1:
                    row[i], col[j] = row[i]+1, col[j]+1
        cnt = 0
        for i, r in enumerate(row):
            for j, c in enumerate(col):
                if mat[i][j] == 1:
                    if col[j] == 1 and row[i] == 1:
                        cnt += 1
        return cnt

        
