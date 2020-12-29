class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0 # 도달해야하는 step 수
        for num in reversed(nums[:-1]): # 뒤에서부터 시작
            max_step += 1 # 도달해야하는 step은 1씩 늘어남
            """만약 현재 index의 num이 step수보다 크다면 끝까지 도달할 수 있으므로 0으로 초기화"""
            if num >= max_step: 
                max_step = 0
            # 안된다면 그 후에 도달해야하는 step이 늘어남.
            
        return True if max_step == 0 else False
