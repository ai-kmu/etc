class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if mat[i].count(1)==1 and [mat[k][j] for k in range(len(mat))].count(1)==1:
                        ans += 1
        return ans
