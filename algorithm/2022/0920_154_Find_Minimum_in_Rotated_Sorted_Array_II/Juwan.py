from collections import deque

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            
            return nums[0]
        
        cnt = 0
        
        q = deque(nums)
        
        while q[0] >= q[-1] and cnt < len(nums):
            
            cnt += 1
            q.append(q.popleft())
            
        return q[0]
