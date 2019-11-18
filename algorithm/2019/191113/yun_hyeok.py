class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        count = 0
        M, N = len(matrix), len(matrix[0])
        
        for k in range(M):
            row_sum = [0] * N
            for i in range(k, M):
                vals = collections.defaultdict(int)
                vals[0] = 1
                submat_sum = 0
                for j in range(N):
                    row_sum[j] += matrix[i][j]
                    submat_sum += row_sum[j]
                    count += vals[submat_sum - target]
                    vals[submat_sum] += 1
        return count
