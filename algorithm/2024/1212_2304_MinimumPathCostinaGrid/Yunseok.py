# 솔루션.,..
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp[i][j]는 (i, j) 위치까지의 최소 비용을 저장
        dp = [[float('inf')] * n for _ in range(m)]
        
        # 첫 번째 행 초기화
        for j in range(n):
            dp[0][j] = grid[0][j]
        
        # DP 테이블 채우기
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + moveCost[grid[i-1][k]][j] + grid[i][j])
        
        # 마지막 행의 최소값 반환
        return min(dp[-1])
