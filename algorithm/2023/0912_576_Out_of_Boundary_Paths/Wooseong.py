# cache 쓰면 자동 memoization 해줌
# 참고: https://www.daleseo.com/python-cache/
from functools import cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, r: int, c: int) -> int:
        module = int(1e9 + 7)
        
        @cache
        def dfs(r, c, move):
            # 탈출
            if r < 0 or c < 0 or r >= m or c >= n:
                return 1
            # 더 이상 못 움직임
            if move == maxMove:
                return 0
            
            # 상하좌우로 움직이며 반복
            return (
                dfs(r, c + 1, move + 1) +
                dfs(r, c - 1, move + 1) +
                dfs(r - 1, c, move + 1) +
                dfs(r + 1, c, move + 1)
            )
        
        # 현위치에서 시작
        return dfs(r, c, 0) % module
