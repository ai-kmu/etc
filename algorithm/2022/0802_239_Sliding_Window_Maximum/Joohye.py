# 오답 : deque로 풀이 시도
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
      
        for i in range(len(nums)):
           
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
                q.append(i)
               
            while q and q[0] == i - k:
                q.popleft()
                
            if i >= k-1:
                ans.append(nums[q[0]])
            return ans
    
