class Solution(object):
    def maxJump(self, stones):
        # 답이 정해져있는 case
        if len(stones) == 2 or len(stones) == 3:
            result = stones[-1] - stones[0]
            return result
    
        max_jump = 0

        # 두칸씩 돌을 건너면서 최댓값을 업데이트
        for i in range(len(stones) - 2):  
            jump = stones[i+2] - stones[i]
            max_jump = max(max_jump, jump)
            
        return max_jump
