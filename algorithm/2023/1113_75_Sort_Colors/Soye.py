class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # bubble sort 사용
        n = len(nums)
        for i in range(0, n-1):
            for j in range(0, n-1-i):
                if nums[j] > nums[j+1]:
                    tmp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp
