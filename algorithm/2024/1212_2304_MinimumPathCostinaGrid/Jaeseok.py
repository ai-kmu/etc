# DP 문제

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 첫 줄을 제외하고는(cost가 고정이므로) 이론상 최댓값보다 크게 설정하여 갱신하도록 함
        dp = [[10 ** 10] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = grid[0][i]

        # 이전 row에서까지 누적된 cost와 경로 cost를 고려했을 때 더 작은 cost로 갱신하도록 점화식을 짬
        for j in range(1, m):
            for k in range(n):
                for l in range(n):
                    dp[j][k] = min(dp[j][k], dp[j-1][l] + grid[j][k] + moveCost[grid[j-1][l]][k])

        # 마지막 줄에서 최솟값이 최소 cost 경로
        return min(dp[-1])
        
