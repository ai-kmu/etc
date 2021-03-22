class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # 땅인 곳만 표시
        land = set((i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if not val)
        def is_closed(x, y):
            # 물이면 그냥 바로 True 리턴
            if (x, y) not in land:
                return True
            
            # 땅이면 해당 위치 먼저 삭제
            land.remove((x, y))
            # 현재 위치를 기준으로 주변도 모두 땅인지 확인
            # 만약 하나라도 물이면 False 즉, 주변에 땅이 있는지 확인 모두 물이면 섬!
            neighbors_closed = is_closed(x+1, y) & is_closed(x-1, y) & is_closed(x, y+1) & is_closed(x, y-1)
            return neighbors_closed and x not in [0, rows-1] and y not in [0, cols-1]
        
        closed = 0
        while land:
            closed += is_closed(*next(iter(land)))
        return closed
