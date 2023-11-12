# 솔루션 참고했으므로 리뷰 안해주셔도 됩니다

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 0의 마지막 인덱스, 현재 위치, 2의 첫 인덱스
        low, mid, high = 0, 0, len(nums) - 1

        # mid가 high보다 작거나 같을때 반복
        while mid <= high:
            # 현재 0일때
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            # 현재 1일때
            elif nums[mid] == 1:
                mid += 1
            # 현재 2일때
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
