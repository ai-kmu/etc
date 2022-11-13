# dp로 풀어보려다 실패..

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

        dp[0][0] = [1, 1] if grid[0][0] == 1 else [0, 0]

        flag = False
        for i in range(1, n):
            if flag:
                dp[i][0] = [-1, -1]
            elif grid[i][0] == 1:
                num = dp[i-1][0][0] + 1
                dp[i][0] = [num, num]
            elif grid[i][0] == -1:
                dp[i][0] = [-1, -1]
                flag = True
        
        flag = False
        for i in range(1, n):
            if flag:
                dp[0][i] = [-1, -1]
            if grid[0][i] == 1:
                num = dp[0][i-1][0] + 1
                dp[0][i] = [num, num]
            elif grid[0][i] == -1:
                dp[0][i] = [-1, -1]
                flag = True
        
        for i in range(1, n):
            for j in range(1, n):
                if grid[i][j] == -1 or (dp[i][j-1] == [-1, -1] and dp[i-1][j] == [-1, -1]):
                    dp[i][j] = [-1, -1]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i][j-1][1], dp[i-1][j][0] + dp[i][j-1][0])
                    if grid[i][j] == 1:
                        dp[i][j] = [dp[i][j][0]+1, dp[i][j][1]+1]
        
        return max(dp[n-1][n-1][1], 0)   
