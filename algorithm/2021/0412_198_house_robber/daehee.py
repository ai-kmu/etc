class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length==0:                         # length 0~2까지 처리하기
            return 0
        elif length==1:
            return nums[0]
        elif length==2:
            return max(nums[0], nums[1])

        dp = [0 for i in range(length)]
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0]+nums[2]
        
        for i in range(3, length):            # dp로 징검다리 식으로 더하기
            dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])
            
        return max(dp)                        # max값 구하기
