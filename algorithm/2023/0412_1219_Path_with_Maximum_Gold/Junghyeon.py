'''
backtracking 이용
O(mn) -> 15^2이라 타임아웃 x
'''
class Solution:
    def getMaximumGold(self, grid):
        # 가로, 세로 길이 저장
        m, n = len(grid), len(grid[0])
        # 방문 확인을 위한 배열
        visited = [[False] * n for _ in range(m)]
        max_gold = [0]

        def dfs(i, j, gold):
            # 범위를 벗어나거나 / 이미 방문했거나 / 해당 위치에 골드가 없으면 리턴
            if m <= i or i < 0 or n <= j or j < 0 or visited[i][j] or grid[i][j] == 0:
                return
            visited[i][j] = True
            # 골드 값 누적
            gold += grid[i][j]
            # 최댓값 업데이트
            max_gold[0] = max(max_gold[0], gold)
            dfs(i+1, j, gold)
            dfs(i-1, j, gold)
            dfs(i, j+1, gold)
            dfs(i, j-1, gold)
            # backtracking
            visited[i][j] = False
        
        # BFS 진행
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    dfs(i, j, 0)

        return max_gold[0]
