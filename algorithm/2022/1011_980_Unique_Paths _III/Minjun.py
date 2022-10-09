class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sp = []
        answer = 0
        move = [-1,1]
        
        for i, gri in enumerate(grid):
            for j, g in enumerate(gri):
                if sp:
                    break
                if g == 1:
                    sp.append((i,j))
                    
        
        def dfs(visit_grid, i, j):
            print("시작", visit_grid, i, j)
            # 인덱스
            if i < 0 or i > len(grid)-1:
                return
            # 인덱스
            if j < 0 or j > len(grid[0])-1:
                return
            # 장애물
            if grid[i][j] == -1:
                return
            
            # 목적지 도착했을 때,
            if grid[i][j] == 2:
                # 목적지 방문처리
                print("도착")
                visit_grid[i][j] = -1
                # 모든 곳 방문 했는지 확인.
                for _ in visit_grid:
                    if 0 in _:
                        break
                # 다 방문 했으면 굳.
                answer += 1
            
            print("방문처리", i,j)
            visit_grid[i][j] = -1
            
            for m in move:
                dfs(visit_grid, i+m, j)
                dfs(visit_grid, i, j+m)
                
        dfs(grid,sp[0][0],sp[0][1])
        return answer
        
            
            
            
            
            
            
            
