class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        cnt = 0
        idx = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            cnt += 1
            idx = i
            nums[i] = -nums[i]
            if cnt == k:
                return sum(nums)
        
        nums.sort()
        while cnt < k:
            nums[0] = -nums[0]
            cnt += 1

        return sum(nums)
