class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):    # 마지막 직전까지 도달할 수 있는지 거꾸로 확인
            if nums[i] + i >= idx:              # 도달할 수 있으면 거기까지 도달할수 있는지 갱신
                idx = i
        answer = True if idx==0 else False
        return answer
