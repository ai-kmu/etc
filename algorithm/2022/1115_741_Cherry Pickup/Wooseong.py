'''
dfs를 두 번 하는 문제.
내려갈 때 최대한 많이 집으면서 grid 갱신하고
올라올 때도 최대한 많이 집으면 됨.
-> 두 번 내려가면 되나?
'''

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)

        # 아래나 오른쪽으로 갈 수 있음
        dd = [(1, 0), (0, 1)]

        # 시간초과 -> 캐싱
        @lru_cache(None)
        def DP(r1, c1, r2, c2):
            # 바깥 or 벽
            if (r1 >= N or r2 >= N or c1 >= N or c2 >= N or
                grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return -inf

            # 첫 번째 경로에서 체리 줍기
            result = grid[r1][c1]

            # 두번째 경로에서 체리 줍기
            if r1 != r2 or c1 != c2:
                result += grid[r2][c2]
            
            # 끝
            if not (r1 == N-1 and c1 == N-1):
                result += max(DP(r1 + dr1, c1 + dc1, r2 + dr2, c2 + dc2)
                              for dr1, dc1 in dd
                              for dr2, dc2 in dd)
            
            return result
        

        answer = DP(0, 0, 0, 0)

        return 0 if answer == -inf else answer
