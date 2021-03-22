class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        
        def dfs(x,y):                                    # 연결된 0인 지점들을 찾아내는 함수 dfs
            if -1 < x and x < w and -1 < y and y < h:
                if grid[y][x] == 0:
                    grid[y][x] = 1
                    dfs(x-1, y)
                    dfs(x,y-1)
                    dfs(x+1,y)
                    dfs(x,y+1)
        
        for i in range(h):
            for j in range(w):
                if i==0 or i==h-1 or j==0 or j==w-1:     # 외곽에 0인 곳과 그에 연결된 곳들은 1로 처리
                    if grid[i][j] == 0:
                        dfs(j,i)
        
        answer = 0
        for i in range(1,h-1):                      
            for j in range(1,w-1):
                if grid[i][j]==0:                        # 내부에 둘러쌓인 0인 지점들을 처리
                    dfs(j,i)
                    answer += 1
        
        return answer
