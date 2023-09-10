class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        # dp 구성
        # row, col, ball_count, tmp 
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        dp[startRow][startColumn][0] = 1
        answer = 0

        # maxMove번 만큼 이동
        for _ in range(maxMove):
            # 4 방으로 공이 갈 수 있는곳에 공 보내기
            for i in range(m):
                for j in range(n):
                    # 공이 없으면 continue
                    if dp[i][j][0] == 0:
                        continue
                    # 공 이동
                    for di, dj in [[1, 0],[0, 1],[-1, 0],[0, -1]]:
                        # 범위 밖이면
                        if i + di < 0 or j + dj < 0 or i + di >= m or j + dj >= n:
                            answer += dp[i][j][0]
                            continue
                        dp[i + di][j + dj][1] += dp[i][j][0]
                    # 이동시켰으니 원래위치 공 제거
                    dp[i][j][0] -= dp[i][j][0]

            # 이동한 값을 dp 로 사용하기 위해 0번 idx로 이동
            for i in range(m):
                for j in range(n):
                    dp[i][j][0] += dp[i][j][1]
                    dp[i][j][1] = 0

        return answer % (10**9 + 7)
