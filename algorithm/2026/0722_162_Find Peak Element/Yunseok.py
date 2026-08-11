class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # 오른쪽 원소가 더 크면 오른쪽으로 이동
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # 현재 원소가 오른쪽 원소보다 크거나 같으면 왼쪽으로 이동
            else:
                right = mid
                
        return left
