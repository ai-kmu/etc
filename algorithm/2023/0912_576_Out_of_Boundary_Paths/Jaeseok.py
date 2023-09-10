# 시간 초과
# 같은 경로를 여러번 탐색하기 때문에 반복되는 경로 때문인 것으로 추정
from collections import deque
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        paths = [[0] * n for _ in range(m)]
        # print(paths)
        answer = 0
        q = deque()
        q.append((startRow, startColumn, 0))
        while q:
            r, c, mv = q.popleft()
            if mv > maxMove:
                continue
            elif r >= m or r < 0 or c < 0 or c >= n:
                answer += 1
                continue
            else:
                q.append((r - 1, c, mv + 1))
                q.append((r, c - 1, mv + 1))
                q.append((r + 1, c, mv + 1))
                q.append((r, c + 1, mv + 1))

        return answer % (10 ** 9 + 7)

# 정답보고 공부했습니다 리뷰 x

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # maxMove를 새로운 축으로 만들어서 3차원 DP 선언
        dp = [[[-1] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        # DP + DFS
        def dfs(x, y, maxMove):
            # maxMove를 초과하는 곳은 탐색하지 않음
            if maxMove < 0:
                return 0

            # boundary를 벗어나면 정답인 경로이므로 1을 return
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1

            # 이미 탐색한 곳은 다시 탐색하지 않고 그때까지 가능했던 정답 경로를 더해줌(DP)
            if dp[x][y][maxMove] != -1:
                return dp[x][y][maxMove]

            # recursive하게 탐색을 진행하면서 현재 경로에서 가능한 모든 정답 경로의 갯수를 탐색함
            dp[x][y][maxMove] = dfs(x - 1, y, maxMove - 1) + dfs(x, y - 1, maxMove - 1) + \
                                dfs(x + 1, y, maxMove - 1) + dfs(x, y + 1, maxMove - 1)
            return dp[x][y][maxMove]

        # 현재 위치부터 탐색 시작
        return dfs(startRow, startColumn, maxMove) % (10**9 + 7)
