# 무식한 접근법...
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # for i in range(le)
        special_cnt = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j])
                if mat[i][j] == 1:
                    is_special = True
                    for idx_i in range(len(mat)):
                        if idx_i == i:
                            continue
                        if mat[idx_i][j] == 1:
                            is_special = False
                            break
                    for idx_j in range(len(mat[0])):
                        if idx_j == j:
                            continue
                        if mat[i][idx_j] == 1:
                            is_special = False
                            break

                    if is_special:
                        special_cnt += 1
   
        return special_cnt
