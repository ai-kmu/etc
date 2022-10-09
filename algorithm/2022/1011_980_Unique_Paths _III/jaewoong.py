# 방법을 찾지 못해 정답을 보고 공부하였습니다...
# 다음과 같은 문제를 백트래킹으로 풀때
# DFS를 조금 변형하여 방문한 곳을 True로 해주고 dfs해준뒤 False로 바꿔주어 백트래킹할 수 있다는 것을 알았습니다...
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row_movements = [1, -1, 0, 0] # row 방향
        col_movements = [0, 0, 1, -1] # col 방향
        ans = 0 # 정답
        max_row = len(grid)
        max_col = len(grid[0])
        total = max_row * max_col # 블록을 채운 최대 하는 길이.
        
        for r in range(max_row):
            for c in range(max_col):
                if grid[r][c] == -1: # 장애물이 있는 블록을 치운다.
                    total -= 1

        def backtrack(row, col, visited, current_count): # 현재 row,col, 방문한 인덱스, 현재 통과한 블록 수 입니다.
            nonlocal ans
            if grid[row][col] == 2 and current_count >= total: 
                ans += 1
            for i in range(4): # 4방향 이동
                r = row + row_movements[i]
                c = col + col_movements[i]
                if 0 <= r < max_row and 0 <= c < max_col and grid[r][c] != -1 and not visited[r][c]: # 범위안에 있고, 장애물이 아니거나 방문하지 않았을떄
                    visited[r][c] = True # 방문한 곳을 True로 바꿔주고
                    backtrack(r, c, visited, current_count + 1) # DFS연산 후
                    visited[r][c] = False # 방문한 값을 백트래킹하여 역추적

        for r in range(max_row):
            for c in range(max_col):
                if grid[r][c] == 1: # 시작인덱스 찾는다
                    visited = [[False] * max_col for _ in range(max_row)]
                    visited[r][c] = True # 시작인덱스를 True로 설정
                    backtrack(r, c, visited, 1) # 시작 인덱스부터 시작
                    return ans
