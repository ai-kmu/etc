class Solution:
    def sortColors(self, nums: List[int]) -> None:

        # nums에는 빨강, 흰색 또는 파랑으로 색칠된 n개의 객체
        # 0, 1, 2를 사용하여 빨, 흰, 파를 나타냄

        l, m, h = 0, 0, len(nums) - 1
        
        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1

        return nums
