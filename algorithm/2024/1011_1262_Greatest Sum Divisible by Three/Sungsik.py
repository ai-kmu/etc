class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        # dp는 현재 위치까지의 값들 중 modular가 0, 1, 2인 max sum을 저장
        dp = [[0, 0, 0] for _ in range(n)]
        
        remain = nums[0] % 3
        dp[0][remain] = nums[0]
        
        for i, num in enumerate(nums[1:]):
            dp[i+1] = dp[i].copy()
            for prev_val in dp[i]:
                new_val = num + prev_val
                new_remain = new_val % 3
                # 현재 값을 사용하는 것이 modular가 동일한 이전 max sum보다 클 경우
                # 이를 반영함
                if new_val > dp[i+1][new_remain]:
                    dp[i+1][new_remain] = new_val
                    
        return dp[-1][0]
    
