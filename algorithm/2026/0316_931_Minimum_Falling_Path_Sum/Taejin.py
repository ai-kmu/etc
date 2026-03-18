class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # 길이 저장
        n = len(matrix)
        
        # 맨 위는 고정, 1부터는 아래 3개 윈도우에서 최솟값을 행렬에 더함.
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(matrix[i - 1][max(0, j - 1):min(j + 2, n)])

        return min(matrix[n - 1])
