'''
네덜란드 국기 문제 공부
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        mid = 0
        end = len(nums) - 1
        pivot = 1

        # i, j 를 바꿔줌
        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while mid <= end:
            # 현재 요소 0일 때,
            if nums[mid] < pivot:
                swap(nums, start, mid)
                start += 1
                mid += 1
            # 현재 요소 2일 때,
            elif nums[mid] > pivot:
                swap(nums, mid, end)
                end = end - 1
            # 현재 1일 때,
            else:
                mid += 1
