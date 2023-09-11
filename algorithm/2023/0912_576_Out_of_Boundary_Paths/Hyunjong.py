MOD = 10**9 + 7
class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):


        # dp 초기화
        dp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        # 초기값 설정
        dp[startRow][startColumn][0] = 1
        result = 0

        # 움직이는 방향 설정
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 최대 이동
        for move in range(1, maxMove + 1):

            # 행렬 탐색
            for i in range(m):
                for j in range(n):
                    # 가능함 움직임
                    for dx, dy in moves:
                        x, y = i + dx, j + dy
                        # 그리드 내에 있는지 확인하고
                        if 0 <= x < m and 0 <= y < n:
                            # 바운더리 내에 있을 때
                            dp[i][j][move] += dp[x][y][move - 1]
                            dp[i][j][move] %= MOD
                        else:

                            # 바운더리 벗어날 때
                            result += dp[i][j][move - 1]
                            result %= MOD
        return result
