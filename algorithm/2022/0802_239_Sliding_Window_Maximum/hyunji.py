# 시간초과
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        
        while len(nums) >= k:
            answer.append(max(nums[:k]))
            nums.pop(0)
            
        return answer
