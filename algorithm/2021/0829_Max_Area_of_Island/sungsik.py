class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        difs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # bfs를 이용해서 섬의 넓이를 구함
        def bfs(r, c, area):
            # 현재 위치가 1일 경우
            if (0 <= r < len(grid) and 0 <= c < len(grid[0])) and grid[r][c] == 1:
                # visit한 기록을 남기기 위해 현재 위치를 0으로 설정
                grid[r][c] = 0
                # 입력받은 area에 1을 추가
                area += 1
                # 상하좌우 방향에서 재귀적으로 bfs를 호출해 넓이를 구함
                for dr, dc in difs:
                    area = max(area, bfs(r+dr, c+dc, area))
                return area
            # 현재 위치가 0이거나 index에서 벗어날 경우 그냥 area를 출력
            return area
        
        answer = 0
        # 모든 위치를 순회하면서 1을 발견할 경우 해당 섬의 넓이를 구함
        # 기존 넓이보다 넓을 경우 업데이트
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    answer = max(answer, bfs(r, c, 0))
        return answer
