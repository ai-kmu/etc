#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = []
        answer = []
        #deque를 이용하여 필요한 값만 가져올 예정
        for i, n in enumerate(nums):
            # 첫번째 요소가 window를 벗어나는 경우
            if deque and i - deque[0] == k: 
                deque.pop(0)

            # deque의 마지막에서 쓸모없는 원소를 제거
            while deque and n > nums[deque[-1]]: 
                deque.pop()
                
            deque.append(i)

            # deque에 올라온 값들을 정답에 추가
            if i >= k - 1: 
                answer.append(nums[deque[0]])
        return answer

