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
