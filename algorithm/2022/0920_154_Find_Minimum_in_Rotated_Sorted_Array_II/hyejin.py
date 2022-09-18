class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        right = len(nums) - 1
        left = 0
        while left < right:
            mid = (right + left) // 2
            if nums[left] == nums[right] == nums[mid]: # 같은 값일 경우, 양 옆을 한칸씩 이동
                left += 1
                right -= 1
            elif nums[mid] > nums[right]: # mid 오른쪽에 min 존재
                left = mid + 1
            else: # mid 왼쪽에 min 존재
                right = mid
        
        return nums[left]
