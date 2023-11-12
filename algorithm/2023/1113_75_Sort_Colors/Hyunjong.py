class Solution:
    def sortColors(self, nums):
        red_count, blue_count, white_count = 0, 0, 0

        # 하나씩 요소를 세기
        for i in nums:
            if i == 0:
                red_count += 1
            elif i == 1:
                white_count += 1
            else:
                blue_count += 1

        # 요소를 바꾸기
        for i in range(len(nums)):
            if red_count != 0:
                nums[i] = 0
                red_count -= 1
            elif white_count != 0:
                nums[i] = 1
                white_count -= 1
            else:
                nums[i] = 2
                blue_count -= 1
