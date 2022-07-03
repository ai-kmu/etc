class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        # nums에 2개 이하일때는 바로 리턴해줄 수 있음
        
        answer = 0
        
        if n == 1:
            answer = nums[0]
            return answer
        if n == 2:
            answer = max(nums[0], nums[1]) 
            return answer
        
        # len(nums) >= 3 일때,
        # dp를 활용하여 푸는데, House Robber 1에서는
        # 하나의 DP 배열로 풀 수 있지만, 이번 문제에선 원형의 자료형이기 때문에
        # 두 배열을 선언하여 풀이
        # 조건은 nums의 맨 첫 요소를 훔치느냐 아니냐에 따라 다름.
        dp1 = [0]*n 
        dp2 = [0]*n 
        
        dp1[0] = nums[0]
        dp2[0] = 0 
        
        dp1[1] = max(nums[0], nums[1])
        dp2[1] = nums[1]
        
        dp2[2] = max(nums[1], nums[2])
        
        """
        dp1 = [nums[0], max(nums[0],nums[1]), ... ]
        dp2 = [0, nums[1], max(nums[1],nums[2]), ... ]
        
        이런식으로 초기화될 것임.
        
        """
       
        
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
            
        for i in range(3, n-2):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])
        
        answer = max(dp1[n-2], nums[n-1]+dp2[n-3])
        
        return answer
