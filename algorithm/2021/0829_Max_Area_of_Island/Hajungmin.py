class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # row, column
        R = len(grid)
        C = len(grid[0])
        
        def area(r,c):
            # r과 c가 범위를 넘으면 return 0
            if r<0 or c<0 or r>=R or c>=C: return 0
            # 만약 해당 그리드의 값이 0이면 return 0
            if grid[r][c]==0: return 0
            # 만약 그리드의 값이 1이면 0으로 바꿔줌
            if grid[r][c]==1: grid[r][c]=0 
            # 0으로 바꿔준 지점부터 dfs 실행, 1을 더해주는 이유는 처음 지점에서도 바꿔줬기 때문에
            return area(r+1,c) +  area(r-1,c) +  area(r,c+1) +  area(r,c-1) + 1 
        max_area = 0
        # 그리드를 모두 돌며 가장 넓이가 넓은 섬을 조사
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    max_area=max(max_area,area(r,c))
                    
        return max_area
