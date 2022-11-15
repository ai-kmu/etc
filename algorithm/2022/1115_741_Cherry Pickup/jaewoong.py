class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def dfs(i_0,j_0,i_1,j_1):
            # 양쪽이 다 끝이면
            if i_0==n-1 and j_0==n-1 and i_1==n-1 and j_1==n-1:
                return grid[n-1][n-1]
            # 범위 벗어나면
            if i_0==0 or j_0==0 or i_1==n or j_1==n:
                return False
            result_1 = dfs(i_0,j_0+1,i_1+1,j_1+1)
            result_2 = dfs(i_0+1,j_0,i_1+1,j_1+1)
            result_3 = dfs(i_0+1,j_0+1,i_1,j_1+1)
            result_4 = dfs(i_0+1,j_0+1,i_1+1,j_1)
            
            ans = max(result_1, result_2, result_3, result_4)
            return ans
