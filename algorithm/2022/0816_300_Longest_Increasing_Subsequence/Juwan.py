class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: 
        
        dp = [1] * len(nums) # 최소 길이가 1이므로, 우선 1로 초기화
        
        for i in range(1, len(nums)): # 가장 첫 번째에 대한 dp table은 이미 1로 구현되었음. 따라서 1부터 시작
            
            for j in range(i): # 처음부터 i까지 검사하면서,
                    
                if nums[i] > nums[j]: # 만약 j보다 i가 크다면
                    
                    dp[i] = max(dp[i], dp[j] + 1) # Subsequence에 해당하며 값을 갱신
                    
        return max(dp)
