#못풀어서 결국 정답 보고 공부했습니다. 리뷰 안해주셔도 됩니다.

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # DFS 함수 정의
        def dfs(x, y):
            # 범위를 벗어나거나, 방문한 적이 없거나, 골드가 없으면 0을 반환
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            
            # 방문한 노드의 값을 0으로 변경하고, 원래 값을 gold 변수에 저장
            gold = grid[x][y]
            grid[x][y] = 0
            
            # 현재 위치에서 갈 수 있는 상, 하, 좌, 우의 위치를 재귀적으로 호출하여 탐색
            max_gold = 0
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                max_gold = max(max_gold, dfs(x+dx, y+dy))
            
            # 방문한 노드의 값을 원래대로 되돌림
            grid[x][y] = gold
            return max_gold + gold
        
        # 모든 시작점에 대해서 DFS를 이용하여 최대값을 구함
        max_gold = 0
        for i in range(m):
            for j in range(n):
                max_gold = max(max_gold, dfs(i, j))
        return max_gold

#BFS로도 풀릴거 같아서 해당 코드도 같이 공부했습니다.
from collections import deque

class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        n, m = len(grid),len(grid[0])
        max_gold = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                  # 현재돈, x,y, visited 로 설정
                    queue = deque([(grid[i][j], i, j, {(i,j)})])
                    while queue:
                        cur_gold, x, y, visited = queue.popleft()
                        # 비교해서 맥스값 업데이트
                        max_gold = max(max_gold, cur_gold)
                        # 각각 돌면서 체크
                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            # 범위 벗어나지않고 방문하지않은곳
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and (nx, ny) not in visited:
                                queue.append((cur_gold + grid[nx][ny], nx, ny, visited | {(nx, ny)}))
        return max_gold
