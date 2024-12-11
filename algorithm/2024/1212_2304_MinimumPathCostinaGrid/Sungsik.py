class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        costs = grid[0].copy()

        for i in range(1, m):
            prev_costs = costs.copy()
            for j in range(n):
                # 현재 위치에서 이전 row의 모든 점에서 오는 cost를 계산하여 최솟값을 계산
                min_cost = float('inf')
                for k in range(n):
                    min_cost = min(prev_costs[k] + moveCost[grid[i-1][k]][j], min_cost)
                
                costs[j] = grid[i][j] + min_cost
        
        return min(costs)
