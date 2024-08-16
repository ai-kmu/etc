class Solution:

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for times in range(k):
            nums.sort()
        
            picked = nums[0]
            picked = -picked

            nums[0] = picked

        return sum(nums)
