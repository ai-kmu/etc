class Solution:
    '''
    시작지점에서부터 dfs를 하면서 도착점에 도달했을때 모든 0을 훑었다면 cnt를 증가시킨다.
    그렇지 않은경우 백트래킹
    '''
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        visited = [[False] * col for _ in range(row)]
        
        zero_cnt = 0
        cnt = 0
        
        for i in range(row):
            for j in range(col):
                # 총 탐색해야할 0의 개수
                if grid[i][j] == 0:
                    zero_cnt += 1
                # 도착지점
                elif grid[i][j] == 2:
                    dest = [i, j]
                # 출발지점
                elif grid[i][j] == 1:
                    start = [i, j]
                    
        def dfs(x, y, zero_cnt):
            nonlocal cnt
            if 0 <= x < row and 0 <= y < col:
                if grid[x][y] != -1 and visited[x][y] == False:
                    # 도착지점에서 모든 0을 훑었을 때
                    if x == dest[0] and y == dest[1] and zero_cnt == -1:
                        cnt += 1
                        return True

                    visited[x][y] = True

                    dfs (x+1, y, zero_cnt-1)
                    dfs (x-1, y, zero_cnt-1)
                    dfs (x, y+1, zero_cnt-1)
                    dfs (x, y-1, zero_cnt-1)

                    visited[x][y] = False
                    
        dfs(start[0], start[1], zero_cnt)
        
        return cnt
