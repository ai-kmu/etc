# Time Limit Exceeded
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        ans = []
        
        for i in range(len(nums)):
            stack.append(nums[i])
            if len(stack) == k:
                ans.append(max(stack))
                stack.popleft()
                
        return ans
