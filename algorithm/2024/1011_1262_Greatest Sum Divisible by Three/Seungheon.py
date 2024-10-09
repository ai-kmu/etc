# solution 보고함
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        dp = [0,0,0]

        for num in nums:
            dp_tmp = dp.copy()
            for dp_i in dp_tmp:
                print(dp_i)
                dp[(dp_i + num) % 3] = max(dp[(dp_i + num) % 3], dp_i + num)

        return dp[0]
