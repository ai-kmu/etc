class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[1000 for i in range(len(nums))]       # dp array 초기화
        dp[0] = 0                                 # 첫번째 element
        for i in range(len(nums)-1):              # 모든 element 비교하면서 가장 짧은 거리 계산하기
            for j in range(i,len(nums)):
                jump = nums[i]                    
                if i+jump < j:                    # jump 거리로 도달할 수 있는 범위만 계산
                    break
                if dp[j]>dp[i]+1:
                    dp[j]=dp[i]+1
                
        return dp[-1]
