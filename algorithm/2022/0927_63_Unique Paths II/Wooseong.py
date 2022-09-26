# 경로의 수 구하는 문제
# 1) 오일러 방법 이용 (사실 상 DP)
class Solution:
    def uniquePathsWithObstacles(self, og: List[List[int]]) -> int:
        ROW = len(og)
        COL = len(og[0])

        euler = [[0 for _ in range(COL)] for _ in range(ROW)]
        
        # 0번째 col들 1로 초기화
        # 중간에 장애물 있으면 그 뒤는 0으로 냅둠
        for r in range(ROW):
            if og[r][0] == 0:
                euler[r][0] = 1
            else:
                break

        # 0번째 row들 1로 초기화
        # 중간에 장애물 있으면 그 뒤는 0으로 냅둠
        for c in range(COL):
            if og[0][c] == 0:
                euler[0][c] = 1
            else:
                break
        
        # 오일러 방법
        # - 한 점까지 가는 방법 = (위에서 내려오기) + (왼쪽에서 오기)
        # 물론 장애물이 없는 점으로만 감
        for r in range(1, ROW):
            for c in range(1, COL):
                if og[r][c] == 0:
                    euler[r][c] = euler[r - 1][c] + euler[r][c - 1]
        
        
        return euler[-1][-1]
      
      
      
      
# 2) 무지성 DFS
# cache: 그냥 돌리면 recursion limit 걸림
# cache 쓰면 자동 memoization 해줌
# 참고: https://www.daleseo.com/python-cache/
from functools import cache

class Solution:
    def uniquePathsWithObstacles(self, og: List[List[int]]) -> int:
        ROW = len(og)
        COL = len(og[0])
        
        @cache
        def dfs(r, c):
            # 넘어가거나 장애물 있으면 0
            if r >= ROW or c >= COL or og[r][c] == 1:
                return 0
            
            # 도착점에 도달하면 1
            if r == ROW - 1 and c == COL - 1:
                return 1
            
            # 오른쪽에서 오기 / 아래에서 오기
            return dfs(r + 1, c) + dfs(r, c + 1)
        
        # 0, 0에서 시작
        return dfs(0, 0)
