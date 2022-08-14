class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        
        for i in range(1, N):
            max_num = dp[i]
            num = nums[i]
            for j in range(i):
                # 현재 num이 이전 num보다 크고 해당 위치에서의 dp값에 1을 더한 값이 최대라면
                # 해당 값으로 max_num을 설정한다
                if nums[j] < num and dp[j] + 1 > max_num:
                    max_num = dp[j] + 1
            dp[i] = max_num
            
        return max(dp)
