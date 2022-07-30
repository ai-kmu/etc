# 첫번째 시도 -> import 없이 코드 짜봤는데 시간 초과

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_num = len(nums) - k + 1
        ans = []
        for i in range(window_num):
            ans.append(max(nums[i:k+i] ))
        return ans
        
# 다음 방법 -> deque 사용

from collections import deque

class Solution():
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        ans = []

        for i in range(len(nums)):
            n = nums[i]
            
            # 슬라이딩 윈도우 이동시키고
            if dq and dq[0] <= i - k: 
                dq.popleft()

            # 기존에 큐 안에 있던 index가 새로 들어오는 index보다 작거나 같으면 오른쪽 pop
            while dq and nums[dq[-1]] <= n: 
                dq.pop()
            dq.append(i)

            if 1 + i >= k: 
                ans.append(nums[dq[0]])

        return ans


