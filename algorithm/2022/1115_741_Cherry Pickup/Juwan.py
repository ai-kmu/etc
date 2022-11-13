class Solution:
        
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        
        n = len(grid)
        
        if n == 1 and grid[0][0] == 1:
            return 1
        elif n == 1 and grid[0][0] == 0:
            return 0
        
        grid_with_path = [ [[0,[]]]*n for _ in range(n) ]

        for i in range(n):
            for j in range(n):                
                grid_with_path[i][j] = [grid[i][j], []]
            
        state = False
        
        for i in range(1, n):
            if grid_with_path[i][0][0] == -1:
                state = True
                
            if state:
                grid_with_path[i][0][0] = 0
            else:
                grid_with_path[i][0][0] += grid_with_path[i-1][0][0]
                grid_with_path[i][0][1].append([i,0])
                grid_with_path[i][0][1].append([i-1,0])
                grid_with_path[i][0][1].extend(grid_with_path[i-1][0][1])
                
        state = False
        
        for i in range(1, n):
            if grid_with_path[0][i][0] == -1:
                state = True
                
            if state:
                grid_with_path[0][i][0] = 0
            else:
                grid_with_path[0][i][0] += grid_with_path[0][i-1][0]
                grid_with_path[0][i][1].append([0,i])
                grid_with_path[0][i][1].append([0,i-1])
                grid_with_path[0][i][1].extend(grid_with_path[0][i-1][1])
        
        
        for i in range(1, n):
            for j in range(1, n):
                
                if grid_with_path[i][j][0] == -1:
                    grid_with_path[i][j][0] = 0
                    continue
                grid_with_path[i][j][1].append([i,j])
                path = grid_with_path[i-1][j][1] if max(grid_with_path[i-1][j][0], grid_with_path[i][j-1][0]) == grid_with_path[i-1][j][0] else grid_with_path[i][j-1][1]
                # print("path :",path)
                grid_with_path[i][j][1].extend(path)
                grid_with_path[i][j][0] += max(grid_with_path[i-1][j][0], grid_with_path[i][j-1][0])
        
        forward_val = grid_with_path[i][j][0]
        

        if not [0,0] in grid_with_path[i][j][1]:
            return 0
        
        for i,j in grid_with_path[i][j][1]:
            grid[i][j] = 0
                        
        for i in range(n-2, -1, -1):
            if grid[i][n-1] == -1:
                break
            grid[i][n-1] += grid[i+1][n-1]
            
        for i in range(n-2, -1, -1):
            if grid[n-1][i] == -1:
                break
            grid[n-1][i+1] += grid[n-1][i+1]    
        
        for i in range(n-2, -1, -1):
            for j in range(n-2, -1, -1):
                if grid[i][j] == -1:
                    continue
                grid[i][j] += max(grid[i+1][j], grid[i][j+1])
        backward_val = grid[0][0]
        
        return forward_val + backward_val
                
                
# 아직 틀린 코드. 푸는 중
