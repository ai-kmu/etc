# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         return nums.index(sorted(nums)[-1])

# 흠 시간제약이 있었군
# 시간 복잡도 고려해서 이진탐색 진행
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # 피크들의 인덱스 중 아무거나 하나만 반환하면 됨
            # mid+1이 더 크면 오른쪽에 무조건 피크 존재
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # 아닐 경우는 왼쪽에 무조건 피크 존재
            else:
                right = mid
                
        # 둘이 같아지는 지점이 피크 인덱스
        return right
