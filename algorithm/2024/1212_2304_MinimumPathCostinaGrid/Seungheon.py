class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        
        # dp 테이블
        dp = [[ float('inf') for _ in grid[0]]for _ in range(len(grid)+1)]
        grid = list(grid)
        grid.append([ 0 for _ in range(len(grid[0]))] ) # 예외처리를 위해 추가

        # 한 줄씩 dp 채우기
        for i, r in enumerate(grid[:-1]):
            for j, num in enumerate(r):
                if i == 0:
                    dp[i][j] = num
                # 이번꺼 + 이동비용 + 다음꺼
                for k, move_cost in enumerate(moveCost[num]):
                    dp[i+1][k] = min(dp[i+1][k], grid[i+1][k] +  move_cost + dp[i][j])

        return min(dp[-2])
