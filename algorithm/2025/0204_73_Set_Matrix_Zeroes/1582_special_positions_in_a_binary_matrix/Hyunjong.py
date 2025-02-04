class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        M, N = len(mat), len(mat[0])

        H_list = []
        W_list = []
        for i in range(M):
            H_list.append(sum(mat[i]))
        print(M, N)

        for j in range(N):
            tmp = 0
            for i in range(M):
                tmp += mat[i][j]
            W_list.append(tmp)
        
        aws = 0
        for i in range(M):
            for j in range(N):
                if H_list[i] == 1 and W_list[j] == 1:
                    if mat[i][j] == 1:
                        aws += 1
        return aws
