# 오답

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        # preprocessing 갈 수 없는곳을 지우기 위함
        new_grid = [[ -1 for i in row ] for row in grid]
        def explore(i= 0, j= 0, reverse = False):

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid):
                return
            if grid[i][j] == -1:
                return
            if new_grid[i][j] > -1:
                return
            new_grid[i][j] = grid[i][j]
            if reverse:
                for dy, dx in [[-1,0],[0,-1]]:
                    explore(i+dy,j+dx,reverse)     
            else:
                for dy,dx in [[1,0],[0,1]]:
                    explore(i+dy,j+dx,reverse)
                    
        explore(0,0,0)
        newgrid_1 = new_grid
        new_grid = [[ -1 for i in row ] for row in grid]
        explore(len(grid)-1,len(grid)-1,True)
        newgrid_2 = new_grid

        for i in range(len(grid)):
            for j in range(len(grid)):
                if newgrid_1[i][j] == newgrid_2[i][j]:
                    grid[i][j] = newgrid_1[i][j]
                else:
                    grid[i][j] = -1    
        
        # preprocessing 한 grid를 이용하여 dp 진행
        
        memo = [ [ 0 for i in row ] for row in grid]
        
        cur_set = set([(0,0)])
        
        while True:
            next_set = set()
            for basic_i, basic_j in list(cur_set):

                # 범위 밖이면 continue
                if basic_i >= len(grid) or basic_j >= len(grid):
                    continue
                # -1 이면 continue
                if grid[basic_i][ basic_j] == -1:
                    continue
                
                # 각 step에서 얻을 수 있는 cherry의 수
                max_cherry = grid[basic_i][basic_j]
                
                # 이전 step의 cherry 수
                up = 0 if basic_i -1 < 0 else memo[basic_i -1][basic_j]
                left = 0 if basic_j -1 < 0 else memo[basic_i][basic_j -1]

                # next step 만들기
                for next_di, next_dj in [[1,0],[0,1]]:
                    if basic_i+next_di >= len(grid) or basic_j+next_dj >= len(grid):
                        continue
                    next_set.add((basic_i+next_di, basic_j+next_dj))
                
                # dp 채워넣기
                for compare_i, compare_j in list(cur_set):
                    # 같은 위치이면 continue
                    if basic_i == compare_i and basic_j == compare_j:
                        continue
                    
                    # max 갱신
                    max_cherry = max(grid[basic_i][basic_j]+grid[compare_i][compare_j] , max_cherry)
                
                # dp 갱신
                memo[basic_i][basic_j] = max_cherry + max(up, left)
                
            # 다음 step을 현재 step으로
            cur_set = next_set
            if not next_set:
                return memo[-1][-1]
