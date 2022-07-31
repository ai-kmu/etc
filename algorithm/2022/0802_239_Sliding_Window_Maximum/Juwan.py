from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if k < 2:
            return nums
        
        
        def get_max_index(b, t): # 최대값의 인덱스 찾는 것
            idx = b
            for j in range(b, t):
                if nums[idx] <= nums[j]:
                    idx = j
            return idx  
        
        answer = []
        
        bot = 0
        top = bot + k - 1 
        
        max_idx = get_max_index(bot, top)
        prev_max = max_idx
        
        while top < len(nums):
                
            if nums[top] >= nums[max_idx]: # 칸 하나씩 움직이면서 그냥 단순 비교하여 최대값을 더하는 과정
                answer.append(nums[top])
                max_idx = top
            else:
                answer.append(nums[max_idx])
                
            bot += 1
            top += 1
            
            if max_idx < bot:
                max_idx = nums.index(max(nums[bot:top]))
                

        return answer # 테스트 케이스는 통과하지만 시간 초과뜸
    
    
# 다 똑같이 deque로 푼 것 같아서 다르게 풀려했으나 실패
    
# 그냥 공부할겸 heapq쓰는 코드 찾아봄
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = None
        
        answer = []
        
        for j in range(0, len(nums) - k + 1): # 처음부터 윈도우가 생성되는 길이까지 루프를 도는데
            
            if j == 0: # 만약 첫번째 윈도우일 때
                
                window = [(-n, i) for i, n in enumerate(nums[:k])] # 최대 힙 구현을 위해 음수로..
                heapify(window) # 해당 윈도우를 힙으로 만들고
                answer.append(-window[0][0]) # 가장 첫번째 원소를 반환할 때 음수를 붙여 최대값이 반환되도록 함
            else: 
                heappush(window, (-nums[j-1+k], j-1+k)) # 그 다음부터는 (음수로 변환한 값, 인덱스) 를 힙 구조에 넣고
                while window[0][1] < j: # 최대값의 인덱스가 j보다 크거나 같을 때 까지 계속 꺼냄.
                    heappop(window)
                answer.append(-window[0][0]) # 정답에 추가해주면 됨
        return answer
