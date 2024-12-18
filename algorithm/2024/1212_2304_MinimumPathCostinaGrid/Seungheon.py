# fail code
# 리뷰 ㄴㄴ

class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        

        dp = [[ float('inf') for _ in grid[0]]for _ in range(len(grid)+1)]
        grid = list(grid)
        grid.append([ 0 for _ in range(len(grid[0]))] )

        print(grid)
        # 한 줄씩
        for i, r in enumerate(grid[:-1]):
            for j, num in enumerate(r):
                if i == 0:
                    dp[i][j] = num
  
                for k, move_cost in enumerate(moveCost[num]):

                    dp[i+1][j] = min(dp[i+1][j], grid[i+1][j] +  move_cost + dp[i][j])
                    # 최솟값
            print(dp)

        return min(dp[-1])
