class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]

        # 양쪽에 nums를 1추가하고 dp로 이용하면 해결될 것 같다고 생각하는데
        # dp를 어떻게 정의해야 할지 모르겠음

        for i in range(len(nums)):
            for j in range(len(nums)):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] + nums[i][j]

        return 0
