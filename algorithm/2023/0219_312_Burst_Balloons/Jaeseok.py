# DP 초기값을 어떻게 설정해야할 지 잘 모르겠음
# 2차원 DP를 사용하더라도 최적의 조건(점화식)을 어떻게 구해야 할 지 모르겠음
# 더 풀어보겠습니다..

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        # nums의 양옆에 자리가 없을 경우를 1로 대체
        nums = [1] + nums + [1]
        dp = [[0] * (n+1) for _ in range(n+1)]
        # 초기화가 이게 맞지는 않는 듯..
        for i in range(1, n):
            dp[i][0] = nums[i-1]*nums[i]*nums[i+1]

        for i in range(1, n):
            for j in range(1, n):
                # 점화식???
                dp[i][j] = max(dp[i][j-1], nums[i-1]*nums[i]*nums[i+1] )
        return 0
