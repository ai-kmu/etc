class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # 0층부터 시작
        prev_accum = grid[0]
        for level in range(1, rows):
            # 다음 층에 도착했을 때 dp 결과 (그 cell에 도달하는 min cost)
            curr_accum = [float('inf') for _ in range(cols)] 
            for prev in range(cols):
                for curr in range(cols):
                    # 누적되어야 할 값은 다음과 같이 `현재 누적 + 이동 + 다음 cell 값`
                    step = (
                        prev_accum[prev]           # 1. 이전 층 cell에 누적된 값
                        + moveCost[                # 2. 이동 비용인데
                            grid[level - 1][prev]  #   from : 이전 층 cell의 index
                        ][curr]                    #   to   : 다음 층의 j번째 cell
                        + grid[level][curr]        # 3. 다음 층 cell의 j번째 cell의 index == 다음 cell 값
                    )
                    # 이전 층의 몇 번째 cell에서
                    # 다음 층의 j번째 cell로 이동하는 게 최소인지 계산하게 됨
                    curr_accum[curr] = min(curr_accum[curr], step)
            
            # 다음 층으로 이동
            prev_accum = curr_accum
        
        # 마지막 층에서 최솟값이 정답임
        return min(prev_accum)
