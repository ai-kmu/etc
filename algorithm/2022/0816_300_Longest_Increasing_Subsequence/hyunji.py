class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 1로 초기화된 dp 배열 선언
        dp = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            max_v = 0
            # i보다 이전 index를 탐색하면서, num[i]보다 값이 더 작은 값들 중에
            # dp 값이 가장 큰 값을 max_v로 지정해준다
            for j in range(i):
                if nums[j] < nums[i]:
                    max_v = max(max_v, dp[j])
            dp[i] = max_v + 1
                    
        return max(dp)
