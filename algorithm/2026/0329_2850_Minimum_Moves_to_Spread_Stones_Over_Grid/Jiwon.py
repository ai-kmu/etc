class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        empty = []  # 빈 돌 칸 (칸의 위치 기록)
        over = []  # 넘치는 돌 (돌의 위치 기록)

        # === 문제풀이 준비
        for i in range(3):
            for j in range(3):
                # 빈 돌 체크
                if grid[i][j] == 0:
                    empty.append((i, j))
                # 어디서 넘치는지 체크
                elif grid[i][j] > 1:
                    for _ in range(grid[i][j] - 1):
                        over.append((i, j))  # 3개 들어 있으면 두 개 옮길 수 있으니까 해당 위치 두 번 등록
        
        # === DFS 준비
        used = [False] * len(over)

        # 맨해튼 거리 (minimum move: 최단 거리)
        def dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        # === DFS
        def dfs(idx):
            # 빈칸 다 채우면 끝
            if idx == len(empty):
                return 0

            ans = 999

            for i in range(len(over)):
                if used[i]:
                    continue

                used[i] = True
                ans = min(ans, dist(over[i], empty[idx]) + dfs(idx + 1))
                used[i] = False

            return ans
        return dfs(0)
