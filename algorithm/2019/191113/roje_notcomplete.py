class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ans = 0
        sums = [[0 for x in range(len(matrix))] for y in range(len(matrix))]
        
        for i, j in enumerate(matrix):
            for x, y in enumerate(j):
                if x==0:
                    sums[i][x] = matrix[i][x]
                else:
                    sums[i][x] = sums[i][x-1] + matrix[i][x]
                    
        for i, j in enumerate(matrix):
            for x, y in enumerate(j):
                if matrix[i][x] == target:
                    ans += 1
                    continue
                    
                    
        return ans
