class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(visited, r,c):
            nonlocal closed
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            visited.add((r,c))
            grid[r][c] = 2
            for i, j in directions: # 4방향에 대해서
                if 0 <= r+i < len(grid) and 0 <= c+j < len(grid[0]): # 범위내에 있을 경우에
                    if grid[r+i][c+j] == 0 or grid[r+i][c+j] == 2 and (r+i, c+j) not in visited: # 현재 connected에서 방문하지 않았을 때
                        if r+i == 0 or c+j == 0 or r+i == len(grid)-1 or c+j == len(grid[0])-1: # 끝구간이면 0이면 closed가 아님
                            closed = False
                        dfs(visited, r+i, c+j)
                else:
                    return False
            return True # 한번 다 연결 됐을 때
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==0: #0일 때 연결된 구간을 조사
                    closed = True
                    if dfs(set(), i, j) and closed: # close되어있고, 0이 한번 다 연결된다면 count+1
                        cnt+=1
        return cnt
