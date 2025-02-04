class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """




        def check(row_idx, col_idx):
            if mat[row_idx][col_idx] == 1:
                row_sum = 0
                col_sum = 0
                for i in range(len(mat[0])):
                    row_sum += mat[row_idx][i]
                for i in range(len(mat)):
                    col_sum += mat[i][col_idx]
                if row_sum == 1 and col_sum == 1:
                    return 1
            return 0
            
        answer = 0
        for row_idx, row in enumerate(mat):
            for col_idx, value in enumerate(row):
                answer += check(row_idx, col_idx)

        return answer


class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """



        row_sum = [0 for _ in mat]
        col_sum = [0 for _ in mat[0]]
        
        for row_idx, row in enumerate(mat):
            for col_idx, value in enumerate(row):
                row_sum[row_idx] += value
                col_sum[col_idx] += value

        answer = 0
        for row_idx, row in enumerate(mat):
            for col_idx, value in enumerate(row):
                if mat[row_idx][col_idx] == 1 and row_sum[row_idx] == 1 and col_sum[col_idx] == 1:
                    answer += 1

        return answer
