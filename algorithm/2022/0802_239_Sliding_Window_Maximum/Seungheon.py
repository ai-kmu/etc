from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        answer = []
        deq = deque()
        
        # 범위 [i-k,i],에서 좌측이 항상 가장 높은 deque를 만듬
        # 현재값이 가장 작은값이되도록 deque를 수정하고 현재값을 추가함
        # -> 이렇게하면 deq에는 현재값보다 큰값들만 존재하게됨
        # -> 항상 deq[-1]값이 가장 큰값을 만족함
        for i, num in enumerate(nums):
            
            # deq이 비었으면 추가
            if not deq:
                deq.append((num, i))

            # 현재값이 가장 왼쪽(가장 큰값)보다 크면 deq을 새로만듬
            if num >= deq[0][0]:
                deq = deque()

            # 가장 먼저들어간것이 범위를 벗어나면 pop
            if deq and deq[0][1] <= i - k :
                deq.popleft()
            
            # deq이 있을때, 나중에 들어간 값부터 탐색하여 현재값보다 작은것이 있으면 pop
            while deq and deq[-1][0] <= num:
                deq.pop()
            
            # 현재값 deq에 append
            deq.append((num, i))
            
            # 해당하는 범위에서만 answer에 값추가
            if i >= k-1:
                answer.append(deq[0][0])            
            
        return answer
