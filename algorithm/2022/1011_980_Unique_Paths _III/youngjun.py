# 실패.....
# if r == end[0] and c == end[1] and walk == can_walk + 1 부분에서 recursion error

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        len_r = len(grid)
        len_c = len(grid[0])

        start, end = [0, 0], [0, 0]
        can_walk = 0

        # 시작 위치, 종료 위치, 몇걸음 갈 수 있는지를 설정한다.
        for r in range(len_r):
            for c in range(len_c):
                if grid[r][c] == 1:
                    start[0], start[1] = r, c
                elif grid[r][c] == 2:
                    end[0], end[1] = r, c
                elif grid[r][c] == 0:
                    can_walk += 1

        # visited 초기화
        visited = [[0] * len_c for _ in range(len_r)]
        cnt = 0

        # 깊이 우선 탐색
        # end에 도착하면서, 빈 곳 모두를 지나도록 탐색해야 한다.
        # visited를 넣어줌으로서 경로탐색 도중에 다시 돌아오지 않게 함.
        def dfs(r, c, walk, visited):
            global cnt

            # end에 도착하면서 걸음이 빈 곳 모두를 지나면
            if r == end[0] and c == end[1] and walk == can_walk + 1:
                # cnt에 1을 더하고 탐색 종료
                cnt += 1
                return
            
            # grid 범위 안에 있고 장애물을 지나지 않으며 아직 지나지 않은 칸일 때
            if 0 <= r < len_r and 0 <= c < len_c and grid[r][c] != -1 and visited[r][c] == 0:
                # visited 체크
                visited[r][c] == 1
                # 상하좌우 방향을 통틀어 탐색해준다.
                dfs(r + 1, c, walk + 1, visited)
                dfs(r - 1, c, walk + 1, visited)
                dfs(r, c + 1, walk + 1, visited)
                dfs(r, c - 1, walk + 1, visited)
                # 한칸 뒤로 감
                visited[r][c] == 0

        dfs(start[0], start[1], can_walk, visited)
        
        return cnt
