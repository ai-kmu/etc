'''
monotone que: window를 크기 순으로 정리하여 유지
1. append로 하나 씩 넣음
    - Monotone: 들어올 애보다 작은 거 다 pop
2. window 범위 유지
    - 첫 번째 애의 index가 window의 left를 벗어나면 popleft
3. answer append
    - window의 right가 k - 1을 넘어가는 순간 매번 append
    - 제일 큰 애는 첫 번째 애니까 얠 넣으면 됨
'''


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        예외처리
        1. window와 nums 크기가 같음: 최댓값 하나만 답
        2. k == 1: nums가 답임
        '''
        if len(nums) == k:
            return [max(nums)]
        elif k == 1:
            return nums
        
        mono_que = deque()
        answer = []
        left = 0
        right = 0
        while right < len(nums):
            '''1. 작은 거 pop하고 새로운 거 넣기'''
            while mono_que and nums[right] > mono_que[-1][0]:
                mono_que.pop()
            mono_que.append((nums[right], right))
            
            '''2. window 범위 유지'''
            if mono_que[0][1] < left:
                mono_que.popleft()
            
            '''3. answer append'''
            if right >= k - 1:
                answer.append(mono_que[0][0])
                left += 1
            
            '''반복문을 돌리는 원동력'''
            right += 1
        
        return answer
