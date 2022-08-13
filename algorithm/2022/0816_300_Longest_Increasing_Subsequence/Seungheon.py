class Solution(object):
    def lengthOfLIS(self, nums):
        
        count = [ 0 for _ in nums]
        
        # num 보다 작은 수를 찾아서, 찾은수 + 1을 기록
        for i, num in enumerate(nums): 
            max_point = 0
            for j in range(i,0,-1):
                if nums[j-1] < num:
                    max_point = max(count[j-1], max_point)
                    
            count[i] = max_point + 1
            
        return max(count)
