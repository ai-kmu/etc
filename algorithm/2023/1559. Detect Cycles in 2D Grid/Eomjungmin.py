class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # dfs로 시도했으나 실패

        n = len(grid)
        m = len(grid[0])

        # 방문했던 곳 flag 저장을 위한 grid
        visited = [[False for _ in range(m)] for _ in range(n)]

        def dfs(i,j,v):
            # 현재 위치가 처음 시작 값과 같고 이미 방문한 경우
            # 한 cycle 완성했으므로(제 생각) dfs 함수에서 true 리턴
            if grid[i][j] == v and visited[i][j]:
                return True

            # 방문 true 저장
            visited[i][j] = True
            
            # 상하좌우로 이동할 때 조건과 시작값과 같은 곳에 맞게 이동
            if i+1<n and visited[i+1][j] == False and grid[i+1][j] == v:
                dfs(i+1,j,v)
            if i-1>=0 and visited[i-1][j] == False and grid[i-1][j] == v:
                dfs(i-1,j,v)
            if j+1<m and visited[i][j+1] == False and grid[i][j+1] == v:
                dfs(i,j+1,v)
            if j-1>=0 and visited[i][j-1] == False and grid[i][j-1] == v:
                dfs(i,j-1,v)
            
            # 방문 다시 false 로 flag 초기화
            visited[i][j] = False

            return False

        # 시작점을 for문으로 수행
        for i in range(n):
            for j in range(m):
                # dfs 함수에서 true가 리턴되면 바로 true로 정답 리턴
                if dfs(i,j,grid[i][j]):
                    return True
                    
        # 사이클이 없으면 false 리턴
        return False
