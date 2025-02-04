class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0
        col_mat = list(zip(*mat))

        for r in range(len(mat)):
            if mat[r].count(1) == 1:
                c = mat[r].index(1)
                if col_mat[c].count(1) == 1:
                    cnt += 1

        return cnt
