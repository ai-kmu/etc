# dfs로 1로 둘러쌓인 곳을 찾음

import time


class Solution:
    def dfs(self, mat, x,y):
        if x == -1 or y == -1 or x == len(mat) or y == len(mat[0]):
            return False
        elif mat[x][y] == 1:
            return True
        
        mat[x][y] = 1 # 이거 없으면 depth error 뜸, 한박자 쉬었다 가자

        if(self.dfs(mat,x-1,y) and self.dfs(mat,x+1,y) and self.dfs(mat,x,y-1) and self.dfs(mat,x,y+1)):
            mat[x][y] = 1
            return True
        else:
            mat[x][y] = -1
            return False
            
    
    def closedIsland(self, grid):

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    ans += int(self.dfs(grid,i,j))
        return ans
