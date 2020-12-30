# dp로 품
# 각 위치로부터 갈 수 있는 거리의 최대치를 저장하면서 나아감(그 위치를 skip한거 포함)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = 0
        for n in nums[:-1]:
            dp = max(dp - 1, n)
            if dp == 0:
                return False
        return True
