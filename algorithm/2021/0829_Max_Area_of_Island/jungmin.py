class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # grid의 너비와 높이 길이 저장
        w = len(grid[0])
        h = len(grid)
        islands = list() # 각 섬마다의 넓이를 저장하기 위한 리스트
        
        # grid의 요소마다 요소값이 1이면 dfs 함수에 들어가서 dfs 알고리즘을 이용해
        # 각 섬의 너비를 구한다.
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    a = 0
                    a = Solution.dfs(a,i,j, grid)
                    islands.append(a)
                    
        if islands == []: # 만약 섬이 없는 형태의 입력이 주어지면 0 return
            return 0
            
        return max(islands) # 각 섬의 넓이 값들 중 최고값을 return
    
    # dfs 함수: dfs알고리즘을 이용하여 1값을 가진 섬의 넓이를 구한다.
    # 다만 인덱스 값이 grid의 범위를 벗어난 경우가 있어서는 안된다.
    # 그래서 한 인덱스를 기준으로 상하좌우를 볼 때 grid의 범위도 고려해야함.
    def dfs(area, i, j, grid):
        grid[i][j]=0 # 해당 요소는 탐색했으므로 0으로 값을 바꿔준다.
        area+=1 # 요소값이 1을 볼 때마다 넓이값 1씩 추가
        
        # dfs 수행
        if (i+1 < len(grid)) and (grid[i+1][j] == 1): 
            area = Solution.dfs(area,i+1,j,grid)
        if (j+1 < len(grid[0])) and (grid[i][j+1] == 1): 
            area = Solution.dfs(area,i,j+1,grid)
        if (i-1 >= 0) and grid[i-1][j] == 1:
            area = Solution.dfs(area,i-1,j,grid)
        if (j-1 >= 0) and grid[i][j-1] == 1: 
            area = Solution.dfs(area,i,j-1,grid)

        return area # 한 섬의 최종 넓이값 return
