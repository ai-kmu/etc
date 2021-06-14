class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def fill(i,j,grid):
            if i < 0 or i >= m:
                return
            if j < 0 or j >= n:
                return
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"
            fill(i+1 ,j,grid)
            fill(i-1, j , grid)
            fill(i , j+1 ,grid)
            fill(i , j-1 ,  grid)

        m = len(grid)
        n= len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count+=1
                    fill(i,j , grid)

        return count
