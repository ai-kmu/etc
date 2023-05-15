class Solution:
    def numSquares(self, n: int) -> int:
        # n 이하의 제곱수 중 가장 큰 값(max_sqrt)을 구합니다.
        max_sqrt = int(n ** 0.5)

        # dp[i] : i를 최소 개수의 제곱수의 합으로 표현하는 경우의 수
        # dp[0]은 0으로 초기화합니다.
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # 1부터 n까지 반복합니다.
        for i in range(1, n+1):
            # i 이하의 제곱수 중 가장 큰 값을 구합니다.
            # (max_sqrt 변수를 미리 구해두었기 때문에 계산 시간을 줄일 수 있습니다.)
            for j in range(1, max_sqrt+1):
                # i보다 큰 제곱수는 사용하지 않습니다.
                if i - j*j < 0:
                    break
                # dp[i]를 갱신합니다.
                dp[i] = min(dp[i], dp[i-j*j]+1)

        # n을 최소 개수의 제곱수의 합으로 표현하는 경우의 수를 반환합니다.
        return dp[n]
