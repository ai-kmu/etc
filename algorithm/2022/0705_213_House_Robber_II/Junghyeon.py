class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        시작하는 인덱스를 다르게 하여 두개의 dp 테이블을 만든 후, 최댓값을 리턴
        '''
        # nums의 길이가 3보다 작거나 같다면 하나만 선택 가능
        if len(nums) <= 3:
            return max(nums)
        
        # dp1: nums[1]부터 시작, dp2: nums[0]부터 시작
        dp1 = [0]*(len(nums)-1)
        dp2 = [0]*(len(nums)-1)
        
        dp1[0] = nums[1]
        dp2[0] = nums[0]

        dp1[1] = max(nums[1], nums[2]) 
        dp2[1] = max(nums[0], nums[1])
        
        # 각각의 dp 테이블 업데이트
        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i+1])
            
        for i in range(2, len(nums)-1):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])
        
        return max(dp1[-1], dp2[-1])
