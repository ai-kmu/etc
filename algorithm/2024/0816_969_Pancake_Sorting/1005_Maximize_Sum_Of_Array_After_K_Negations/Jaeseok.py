class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        i = 0
        while i < k:
            nums.sort()
            if nums[0] < 0:
                nums[0] = -nums[0]
            else:
                if (k - i) % 2 == 0:
                    return sum(nums)
                else:
                    nums[0] = -nums[0]
            i += 1
        return sum(nums)
      
