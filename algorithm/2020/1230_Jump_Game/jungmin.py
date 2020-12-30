class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_index = 0
        for i in range(len(nums)):
            if i + nums[i] >= maximum_index:
                maximum_index = i + nums[i]
            
            if maximum_index == i:
                break

        if maximum_index >= nums[len(nums)-1]:
            return True

        elif maximum_index < nums[len(nums)-1]:
            return False

