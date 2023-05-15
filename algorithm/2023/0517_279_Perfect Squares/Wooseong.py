class Solution:
    def numSquares(self, n: int) -> int:
        # 예외처리
        if int(n ** 0.5) ** 2 == n:
            return 1

        # n을 만드는 데 사용할 perfect square 목록
        # n을 만들기 위해 ceil(sqrt(n)) ** 2 보다 큰 수는 필요 없으므로 thold 적용
        thold = int(n ** 0.5 + 2)
        cands = [i ** 2 for i in range(1, min(thold, 101))]

        # Dynamic Programming
        dp = [1 if i in cands else 10000 for i in range(n + 1)]
        dp[0] = 0

        # n까지 돌면서
        for i in range(n + 1):
            # cands에 있는 애와의 조합으로 가능한 애들 중 가장 작은 값 사용
            # dp[i] + 1은 현재 i를 만드는 데 필요한 덧셈에 j를 한 번 더해야 한다는 의미
            for j in cands:
                if i + j <= n:
                    dp[i + j] = min(dp[i] + 1, dp[i + j])
                else:
                    break

        # 답은 dp[n] == dp[-1]
        return dp[-1]
