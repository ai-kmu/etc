class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # 길이 체크
        m = len(grid)
        n = len(grid[0])

        # dfs 함수 정의
        def dfs(r, c, collect):
            # 범위 밖이거나 금이 없거나 방문했거나
            if (r < 0 or r >= m or
                c < 0 or c >= n or
                not grid[r][c] or grid[r][c] > 100):
                return collect
            
            collect += grid[r][c]  # 금 챙기기
            grid[r][c] += 128      # 방문 처리
            
            # 현 위치에서 제일 많이 갖고 올 수 있는 금 양 챙기기
            max_res = 0
            for nr, nc in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
                max_res = max(dfs(nr, nc, collect), max_res)
            grid[r][c] -= 128       # 방문 처리 취소
            return max_res

        return max(dfs(r, c, 0) for c in range(n) for r in range(m))
