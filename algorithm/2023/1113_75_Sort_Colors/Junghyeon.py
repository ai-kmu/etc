'''
포인터 사용
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 0 - red, 1 - white, 2 - blue
        mid_value = 1
        left, cur, right = 0, 0, len(nums)
        while cur < right:
            if nums[cur] < mid_value:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1 
                cur += 1
            elif nums[cur] == mid_value:
                cur += 1
            else:
                right -= 1
                nums[right], nums[cur] = nums[cur], nums[right]
