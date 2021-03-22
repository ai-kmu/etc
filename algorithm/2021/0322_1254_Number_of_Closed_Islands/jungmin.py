class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        visited = [ [0] * n  for i in range(m)] # 방문 여부 표시를 위한 grid 생성
        def dfs(i,j):
            
            ans=True

            # 맨 위쪽 행과 아래쪽 행은 섬을 구성할 수 없음
            if i == 0 or i == m-1:
                ans = False
            
            # 그리고 맨 오른쪽과 맨 왼쪽 행은 섬을 구성할 수 없음.
            if j == 0 or j == n-1:
                ans = False
            
            visited[i][j] = 1 # 다녔다는 표시를 함. 안하면 무한루프 반복할 가능성이 존재.
            
            for x,y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]: # 현재 인덱스 위치에서 위, 아래, 왼쪽, 오른쪽을 탐색한다.
                if 0<=x<m and 0<=y<n and grid[x][y] == 0 and visited[x][y] == 0: # 만약에 탐색하려는 주변 인덱스 위치가 grid 내에 있고 그 인덱스에 해당되는 요소 값이 0이며 방문한 적이 없으면
                    # 계속 깊은 탐색을 한다. 그러다가 어느 순간 주변이 다 1이면 깊은 탐색을 종료.
                    ans &= dfs(x,y) 
            
            return ans
        
        count = 0 # 갯수 세는 변수 초기화
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and visited[i][j] == 0: # grid안에서 어느 요소값이 0이고 방문한 적이 없으면
                    if dfs(i,j): # 깊은 탐색을 시행. 시행한 결과 True값이면 
                        count+=1 # closed island count
                        
                        
        return count # closed island 갯수 출력
