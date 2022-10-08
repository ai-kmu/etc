# bit masking으로 visited 및 종료 조건 처리
# 2진수의 각 자리가 index를 나타냄
# |, &는 각 자리끼리 and, or 연산을 진행
# 0010 | 0001 = 0011
# 0011 & 0101 = 0001
# <<는 비트를 왼쪽으로 이동시킴
# 1 << 3은 000000001을 왼쪽으로 세 칸 밀어서 000001000으로 만듦

# 따라서 1 << ind를 통해 현재 index만 1로 만들 수 있으며
# state | (1 << ind)를 통해 state에 현재 index를 추가하고
# (state & (1 << ind)) == 0를 통해 현재 index를 방문했었는지 판단할 수 있다.

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 종료를 위해 가져야 할 bit state
        end_state = 0
        for r in range(m):
            for c in range(n):
                # 2차원 배열 -> 1차원화
                ind = r * n + c
                # 시작, 끝 점 포함 지나쳐야 하는 길 bit masking
                if grid[r][c] != -1:
                    end_state |= (1 << ind)
                
                # 시작 위치와 state 지정
                if grid[r][c] == 1:
                    start_state = 1 << ind
                    sr, sc = r, c

        answer = 0
        # backtracking을 위한 dfs 함수
        def dfs(r, c, state):
            nonlocal answer

            # 종료 조건
            # 1. 끝 점 도달
            if grid[r][c] == 2:
                # 2. 모든 지점 거침
                if state == end_state:
                    answer += 1
                return

            # 상하좌우 dfs
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr = r + dr
                nc = c + dc
                ind = nr * n + nc
                if ((0 <= nr < m and 0 <= nc < n) and   # 가능한 Index이고
                    (((1 << ind) & state) == 0) and       # 현재 위치가 state에 없으며 = 지났던 곳이 아니며
                    grid[nr][nc] != -1):                # 장애물이 없으면 진행
                    dfs(nr, nc, state | (1 << ind))

        # 시작 지점에서 시작
        dfs(sr, sc, start_state)

        return answer
