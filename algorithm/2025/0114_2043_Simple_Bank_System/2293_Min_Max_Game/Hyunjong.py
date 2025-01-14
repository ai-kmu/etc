from collections import deque
class Solution(object):
    def minMaxGame(self, nums):
        nums = deque(nums)
        aws = 0
        while nums:
            if len(nums) >=4:
                min_f = nums.popleft()
                min_s = nums.popleft()
                max_f = nums.popleft()
                max_s = nums.popleft()
                nums.append(min(min_f, min_s))
                nums.append(max(max_f, max_s))
            elif len(nums) >=2:
                min_f = nums.popleft()
                min_s = nums.popleft()
                nums.append(min(min_f, min_s))
            else:
                aws = nums.popleft()
        
        return aws
            
