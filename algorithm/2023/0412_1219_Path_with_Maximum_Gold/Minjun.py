# testcase에서 막힘

from collections import deque
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        good =[]

                   
        def dfs(m,n):
            q = [(m,n,0)]
            tot = 0
            visited = []
            gold = []
            while q:
                x, y, tot = q.pop()
                visited.append((x,y))
                tot += grid[x][y]
                gold.append(tot)
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (nx,ny) in visited:
                        continue
                    if nx >= len(grid) or nx < 0:
                        continue
                    if ny >= len(grid[0]) or ny < 0:
                        continue
                    if grid[nx][ny] == 0:
                        continue
                    q.append((nx,ny,tot))
                
            return max(gold)
                # tot += grid[nx][ny]
                # if (ny,ny) not in visited: 
                #     visited.append((nx,ny))
                #     gold.append(tot)
                # return tot
        # dfs(0,1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                good.append(dfs(i,j))

        return max(good)
