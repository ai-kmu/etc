# 첫번째 집과 마지막 집은 같이 털 수 없으니까 두 케이스로 나눠서 dp 배열을 선언

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        answer = 0
        
        if len(nums) <= 3:
            return max(nums)
        
        # 첫번째 집은 털지 않는 경우의 dp 배열
        dp_one = [0 for i in range(len(nums)-1)]
        # 마지막 집은 털지 않는 경우의 dp 배열
        dp_last = [0 for i in range(len(nums)-1)]
        
        # 첫번째 집을 제외한 배열
        nums_one = nums[1:]
        # 마지막 집을 제외한 배열
        nums_last = nums[:-1]
        
        # 각 dp 배열의 첫번째 원소 할당
        dp_one[0] = nums_one[0]
        dp_last[0] = nums_last[0]
        
        # dp 배열의 두번째 원소는 index 0, 1 둘 중 돈이 더 많은(max) 집
        dp_one[1] = max(nums_one[0], nums_one[1])
        dp_last[1] = max(nums_last[0], nums_last[1])
        
        # 점화식: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # 두 가지 케이스에 대해서 dp 배열을 채워줌
        for i in range(2, len(nums_one)):
            dp_one[i] = max(dp_one[i-1], dp_one[i-2] + nums_one[i])
            
        for i in range(2, len(nums_last)):
            dp_last[i] = max(dp_last[i-1], dp_last[i-2] + nums_last[i])
            
        answer = max(max(dp_one), max(dp_last))
        
        return answer
