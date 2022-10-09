class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        answer = []
        square = 0
        start = []
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                # 탐색 시작점
                if grid[i][j] == 1:
                    start += [i, j]
                
                # 총 탐색해야하는 square의 수
                if grid[i][j] != -1:
                    square += 1
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        def DFS(x, y, square, answer):
            # 범위 밖으로 index가 나가거나 wall에 위치해있으면 return
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
                return
            
            # 탐색 다 하고, 종료 지점에 도착한 경우
            if grid[x][y] == 2 and square == 0:
                answer.append(1)
                        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                before = grid[x][y]
                # 방문 처리
                grid[x][y] = -1
                # 다음 지점 탐색
                DFS(nx, ny, square-1, answer)
                # 탐색이 끝나고 난 뒤에는 이전 값으로 되돌려줌
                grid[x][y] = before
              
            
        DFS(start[0], start[1], square-1, answer)
                
        return len(answer)
