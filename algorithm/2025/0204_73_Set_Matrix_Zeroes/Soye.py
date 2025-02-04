class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0 
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                check = 0
                if mat[i][j] == 1:
                    for k in range(len(mat)):
                        if mat[k][j] == 1 and k != i:
                            print(i, j)
                            print(k, j)
                            print()
                            check = 1
                            break
                    for k in range(len(mat[i])):
                        if mat[i][k] == 1 and k != j:
                            print(i, j)
                            print(i, k)
                            check = 1
                            break
                if mat[i][j] == 1 and check == 0:
                    print("--", i, j)
                    cnt = cnt + 1
                    
        return cnt
