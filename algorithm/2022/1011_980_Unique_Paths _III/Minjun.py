class Solution:
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.answer = 0
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
        # start point 추출
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    sx, sy = i, j
                    break
        
        def dfs(grid, i, j):
            # 인덱스 범위처리
            if i < 0 or i > len(grid)-1:
                return
            # 인덱스 범위처리
            if j < 0 or j > len(grid[0])-1:
                return
            # 장애물 backtracking
            if grid[i][j] == -1:
                return
            
            # 목적지 도착했을 때,
            if grid[i][j] == 2:
                # 모든 곳 방문 했는지 확인.
                # grid 에 0이 아닌 곳이 있다면, 다 방문한 것이 아님.
                for k in grid:
                    if 0 in k:
                        return
                # 다 방문했으니 경로 개수 +1 후 return
                self.answer += 1
                return
            
            # ======================
            # 경로 탐색 과정
            
            # grid 원상복구용 변수
            temp = grid[i][j]
            
            # grid 방문 처리
            grid[i][j] = -1
            for m,n in zip(dx,dy):
                dfs(grid, i+m, j+n)
                
            # 다른 경로 찾을 때를 대비하여 grid  원상복구
            grid[i][j] = temp
            
        dfs(grid, sx, sy)
        return self.answer
