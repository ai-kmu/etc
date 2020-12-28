class Solution:
    def canJump(self, nums: List[int]) -> bool:
             
        maxArriveInd = 0
        for i in range(len(nums)):
            if i > maxArriveInd: # 최대도달가능 index보다 커버리면 false
                return False
            
            maxArriveInd = max(maxArriveInd, i+nums[i]) # 가장 멀리 jump할 수 있는 인덱스 저장
            if maxArriveInd >= len(nums)-1:  # 최대 갈수 있는 인덱스가 리스트 길이를 넘어서면 true 반환
                return True
