class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        import copy

        # 행과 열 크기 저장
        m = len(grid)
        n = len(grid[0])

        # 획득 가능한 골드 개수들 저장
        ans = []

        # 방문했던 위치 기록
        visited = [[0 for _ in range(n)] for _ in range(m)]

        # dfs 방식으로 가능한 path에서 획득할 수 있는 gold 개수 계산
        def dfs(i,j,gold,check):
            check[i][j] = 1
            if j-1 >= 0 and check[i][j-1] == 0 and grid[i][j-1] != 0:
                dfs(i,j-1,gold+grid[i][j-1],check)
            if j+1 <= n-1 and check[i][j+1] == 0 and grid[i][j+1] != 0:
                dfs(i,j+1,gold+grid[i][j+1],check)
            if i+1 <= m-1 and check[i+1][j] == 0 and grid[i+1][j] != 0:
                dfs(i+1,j,gold+grid[i+1][j],check)
            if i-1 >= 0 and check[i-1][j] == 0 and grid[i-1][j] != 0:
                dfs(i-1,j,gold+grid[i-1][j],check)
            
            # 현재 i,j에서 가능한 path 다 돌았으면 check를 다시 0으로 해야 함
            check[i][j] = 0
            ans.append(gold)


        # 가능한 시작점부터 dfs하여 가능한 gold 수 저장
        for i in range(m):
            for j in range(n):
                check = copy.deepcopy(visited)
                if grid[i][j] != 0:
                    dfs(i,j,grid[i][j],check)

        # 가능한 gold 수들 중 최댓값 return
        # ans가 빈 리스트이면 가능한 gold가 0이므로 0을 return
        if ans == []:
            return 0
        else:
            return max(ans)
