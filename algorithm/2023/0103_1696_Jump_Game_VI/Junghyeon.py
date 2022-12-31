'''
일반적인 dp, O(n*k) -> 시간초과
'''
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # deque 초기화
        deq = deque([[0, nums[0]]])

        for i in range(1, len(nums)):
            # deq가 비어있지않고, slicing 범위 내에 있다면 popleft
            while deq and deq[0][0] + k < i:
                deq.popleft()
            
            tmp = deq[0][1] + nums[i] 
            
            # deq가 비어있지않고, 현재 값보다 작다면 pop
            while deq and deq[-1][1] < tmp:
                deq.pop()
            
            # i번째 까지의 최댓값 저장
            deq.append((i, tmp))
            
        return deq[-1][1]
