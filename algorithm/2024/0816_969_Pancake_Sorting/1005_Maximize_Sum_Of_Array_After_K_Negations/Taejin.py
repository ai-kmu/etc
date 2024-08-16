class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:    
        sorted_nums = list(sorted(nums))

        for _ in range(k):
            sorted_nums[0] = -sorted_nums[0]
            sorted_nums.sort()

        return sum(sorted_nums)
