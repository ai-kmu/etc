# 45까지만 통과됩니다 풀이안해주셔도 됩니다.

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # player 1 : + 방향, player 2 : - 방향 dp
        dp = [float("-inf") for i in range(len(nums) + 1)]
        dp[0] = 0

        def make_dp(i, ns):
            # print(i, ns)
            nonlocal dp
            if dp[i] != float("-inf") or i < 1:
                return dp[i]
            
            else:
                dp[i] = (-1 if i % 2 else 1) * max(ns[0] + make_dp(i - 1, ns[1:]), ns[-1] + make_dp(i - 1, ns[:-1]))
                return dp[i]

        make_dp(len(nums), nums)
        print(dp)
        return (dp[-1] - dp[-2]) >= 0 if len(nums) > 1 else True

        
