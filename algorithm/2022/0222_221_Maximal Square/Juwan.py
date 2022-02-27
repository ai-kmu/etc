class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        h = len(matrix)
        
        w = len(matrix[0])
        
        dp = [[0]*w for _ in range(h)]

        res = 0
        
        for i in range(h):
            for j in range(w):
                dp[i][j] = int(matrix[i][j])
                if dp[i][j]:
                    res = 1
        
        for i in range(1, h):
            for j in range(1, w):
                
            
                if dp[i][j] and dp[i-1][j] and dp[i][j-1] and dp[i-1][j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

                    res = max(res, dp[i][j])

        return res**2

        
