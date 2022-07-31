'''
기본적으로 queue에는 index를 넣는다.
들어올 원소보다 작은 원소들을 pop을 통해 제거하며, 들어올 원소의 index를 append한다.
window의 범위를 유지시키면서, 오른쪽 포인터 + 1이 sliding window의 사이즈보다 커지면 index에 해당하는 수를 answer에 append한다.
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        # 인덱스가 담길 queue 만들어줌
        mono_queue = deque()
        # 포인터 초기화
        l = r = 0

        while r < len(nums):
            # 새로 들어올 숫자 nums[r]이 mono_queue의 마지막 원소(인덱스)보다 작을 경우, 오른쪽 원소부터 차례로 날림
            while mono_queue and nums[mono_queue[-1]] < nums[r]:
                mono_queue.pop()
                
            # mono_queue에 인덱스를 넣어 주며 sliding window 이동한다.
            mono_queue.append(r)
            
            # sliding window 범위를 유지해준다.
            if l > mono_queue[0]:
                mono_queue.popleft()
            
            # 오른쪽 포인터 + 1이 sliding window의 크기와 같거나 커지면, 원소를 answer에 추가시키고 왼쪽 포인터를 이동시켜 sliding window를 이동한다.
            if (r + 1) >= k:
                answer.append(nums[mono_queue[0]])
                l += 1
                
            # 오른쪽 포인터를 이동시킨다.
            r += 1

        return answer
