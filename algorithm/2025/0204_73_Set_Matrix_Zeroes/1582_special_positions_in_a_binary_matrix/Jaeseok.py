class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        answer = 0
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    flag = False
                    for k in range(m):
                        if mat[k][j] == 1 and k != i:
                            flag = True
                    for l in range(n):
                        if mat[i][l] == 1 and l != j:
                            flag = True
                    if flag == False:
                        answer += 1
        
        return answer


class 
