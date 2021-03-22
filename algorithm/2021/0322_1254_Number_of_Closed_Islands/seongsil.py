class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        lenRow, lenCol = len(grid), len(grid[0])
        land = [(i,j) for i, row in enumerate(grid) for j, val in enumerate(row) if not val]  #land(val=1)인 경우의 좌표
        
        def dfs_is_closed(x,y):
            if (x,y) not in land: # land 아닐 경우 true 반환
                return True
            
            land.remove((x,y)) 
            neighbors_closed = dfs_is_closed(x-1, y) & dfs_is_closed(x+1, y) & dfs_is_closed(x, y-1) & dfs_is_closed(x,y+1) # 주변이 모두 true일 경우만 true

            return neighbors_closed and x not in [0, lenRow-1] and y not in [0, lenCol-1] # 모서리에 있는건 land 아니므로 제외
        
        closed_islands = 0

        while land:
            closed_islands += dfs_is_closed(*next(iter(land)))
        return closed_islands
