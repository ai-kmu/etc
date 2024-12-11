# 최소 -> 탐색해야됨
# dfs로 풀면 시간초과날거임
# dp 문제
# 현재에서 (이동 비용 + 다음 셀 값) 최소인 경로를 선택해야 됨

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        # dp 테이블 생성
        # 최소값 찾기 위해 무한대로 생성해놓음
        dp = [[float('inf')] * len(grid[0]) for i in range(len(grid))]
        # 시작점 세팅
        for cell in range(len(grid[0])):
            dp[0][cell] = grid[0][cell]
        # 행마다 최소값 채워넣기
        for row in range(1, len(grid)):
            for prev_cell in range(len(grid[0])):
                prev_cost = dp[row-1][prev_cell]
                prev_idx = grid[row-1][prev_cell] # -> prev_cell에서 현재 셀로 넘어오는 비용 리스트
                for cell in range(len(grid[0])):
                    cost = prev_cost + moveCost[prev_idx][cell] + grid[row][cell]
                    if cost < dp[row][cell]:
                        dp[row][cell] = cost
        return min(dp[-1])

# 밑에는 그리디한 풀이 (이동 비용이 최소인 것) -> 예제만 통과
# class Solution:
#     def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
#         sp = {}
#         route = {}
#         last = grid[-1]
#         ans = float('inf')
        
#         # 첫번째 행에서 시작 마지막 행까지 비용 [최소]
#         for cell in grid[0]:
#             tot = cell
#             row = 0
#             tmp = 0
#             c = cell
#             while c not in last:
#                 # 다음 후보군
#                 idx = -1
#                 # 이동값
#                 tmp = 101
#                 for i, candi in enumerate(moveCost[c]):
#                     # 최소비용
#                     if candi < tmp:
#                         idx = i
#                         tmp = candi
#                 row += 1
#                 c = grid[row][idx]
#                 tot += tmp
#             tot += c
#             if tot < ans:
#                 ans = tot
#         return ans

