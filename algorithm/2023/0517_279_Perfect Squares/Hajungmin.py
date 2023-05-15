class Solution:
    def numSquares(self, n: int) -> int:
        # dp 테이블 선언
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0

        # n 이하의 제곱수들을 모아놓은 리스트 선언
        power_nums = []

        # power_nums 안에 n이하의 수들 중 제곱수를 넣어줌
        for i in range(int(pow(n, 0.5)) + 1):
            power_nums.append(i ** 2)

        # dp 테이블을 돌면서 현재 인덱스인 i에다가 1을 더해준 값과 제곱수를 더해준 i + j에 해당하는
        # 인덱스에 있는 값을 비교해서 더 작은 수로 i + j번째 인덱스의 dp 테이블 업데이트
        # -> 더하는 수의 개수를 최소로 해야하기 때문에
        for i in range(n + 1):
            for j in power_nums:
                # i + j가 dp 테이블 인덱스를 넘어가지 않도록 조건 설정
                if i + j <= n:
                    dp[i + j] = min(dp[i] + 1, dp[i + j])
                else:
                    break

        # dp 테이블의 마지막 수를 정답으로 반환
        return dp[-1]
