class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        self.ans = 0
        m = len(grid)
        n = len(grid[0])
        x = 0
        y = 0
        empty = 1
        
        
        # for문 돌며 시작 지점(x,y)과 이동 가능한 칸을 구한다
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    x = i
                    y = j
                elif grid[i][j] == 0:
                    empty += 1
        
        
        def dfs(x, y, empty):
            print(grid)
            # m, n 범위에 들어가지 않고 음수(-1 이라면 막힌곳 -2라면 이미 조회한 곳)일 때는 리턴
            if not (0 <= x < m and 0 <= y < n and grid[x][y]>=0): return
            
            # 끝 지점에 도착했을 때 이동가능한 구간이 0이라면 모든 구간을 조회한 것 
            if grid[x][y] == 2 :
                if empty == 0:
                    self.ans += 1
                return
            
            # 이미 갔던 곳은 -2로 바꿔줌
            grid[x][y] = -2
            
            # 네 방향 조회
            dfs(x+1, y, empty-1)
            dfs(x-1, y, empty-1)
            dfs(x, y+1, empty-1)
            dfs(x, y-1, empty-1)

            # 다시 이동가능하게 바꿔줌 
            grid[x][y] = 0
        
        dfs(x,y, empty)
        
        return self.ans
            
                
        
            
