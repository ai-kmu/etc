# fail code


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        
        m = len(grid)
        n = len(grid[0])
        grid_sum = 0
        for row in grid:
            grid_sum += sum(row)

        
        def explore(i,j):
            nonlocal m
            nonlocal n

            answer = 0

            # 범위 밖이면
            if i < 0 or j < 0 or i >= m or j >=n :
                return 0
            # 방문했거나 0이면 
            if tmp_grid[i][j] == 0:
                return 0
            
            tmp_grid[i][j] = 0

            answer += 1

            for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
                answer += explore(i+dy, j+dx)

            
            return answer


        for i in range(m):
            for j in range(n):
                if (i, j) == (0,0) or (m-1, n-1) == (0,0):
                    continue
                if grid[i][j] == 0:
                    continue
                tmp_grid = copy.deepcopy(grid)

                # 현재 위치를 0으로 만들고 끊어지는지 확인
                tmp_grid[i][j] == 0

                for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
                    if grid[i+dy][j+dx] == 1:
                        # visit = [[ 0 for _ in range(n)] for _ in range(m)]
                        # 다 연결이 되어있지 않으면 True 를 return 
                        print(explore(i+dy, j+dx))
                        if grid_sum-1 != explore(i+dy, j+dx):
                            return True
                        continue

                tmp_grid[i][j] == 1


        return False
