class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)
	# dp테이블 생성
        dp = [[0]*n for _ in range(n)]
        dp[0][0] = grid[0][0]
        # dp[i][j]: 경로에서 가져올 수 있는 최대 체리 수
	# k는 최대 이동 횟수, 2*n-1 인 경우 최대
        for k in range(1, 2*n-1):
            curr = [[-1]*n for _ in range(n)]
            for i in range(min(n, k+1)):
                if (k-i) >= n or grid[i][k-i] < 0: 
                    continue
                for j in range(min(n, k+1)):
                    if k-j >= n or grid[k-j][j] < 0: 
                        continue
                    ans = dp[i][j]
                    if i > 0: 
                        ans = max(ans, dp[i-1][j])
                    if j > 0: 
                        ans = max(ans, dp[i][j-1])
                    if i > 0 and j > 0: 
                        ans = max(ans, dp[i-1][j-1])
                    if ans < 0: 
                        continue
                    ans += grid[i][k-i]
                    if i != k-j:
                        ans += grid[k-j][j]
                    curr[i][j] = ans
            dp = curr
        return max(dp[-1][-1], 0)
