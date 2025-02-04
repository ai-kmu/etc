class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 1:
                    check = sum(mat[row]) + sum(r[col] for r in mat)
                    if check == 2:
                        cnt += 1

        return cnt
