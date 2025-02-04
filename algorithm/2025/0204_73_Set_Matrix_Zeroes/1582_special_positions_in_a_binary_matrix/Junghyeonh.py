class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        candidate = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    candidate.append([i, j])

        cnt = 0

        if len(candidate) == 1:
            return 1

        for x in range(len(candidate)):
            cnt_a = 0
            for y in range(len(candidate)):
                if x == y:
                    continue
                # print(y, x)
                a = candidate[y]
                b = candidate[x]
                # print(a, b)
                if a[0] != b[0] and a[1] != b[1]:
                    cnt_a += 1
                    if cnt_a == len(candidate)-1:
                        cnt += 1
                    else:
                        continue
                else:
                    break

        return cnt
