class Solution:
    def rob(self, nums: List[int]) -> int:
        # 집이 3개 이하인 경우에는 가장 큰 금액을 털 수 있는 집을 고르기
        if len(nums) <= 3:
            return max(nums)
        
        # dp : 첫 번째 집을 고르는 경우
        # dp2 : 마지막 집을 고르는 경우
        
        n = len(nums)
        # DP 테이블 초기화
        
        dp = [0 for _ in range(n - 1)]
        dp2 = [0 for _ in range(n - 1)]
        
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        dp2[0] = nums[1]
        dp2[1] = max(nums[1],nums[2])
        
        # 점화식 : a[n] = max(a[n-1] , a[n-2] + k[i])
        # 이 때 k는 현재 방문할 집에서 털 수 있는 금액
        
        # 첫 번째 집을 고르는 경우의 dp
        for i in range(2,n - 1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        # 마지막 집을 고르는 경우의 dp
        for i in range(3, n):
            dp2[i-1] = max(dp2[i-3] + nums[i], dp2[i-2])
        
        
        # 두 경우에서 가장 큰 금액을 털 수 있는 쪽 고르기
        return max(max(dp),max(dp2))
