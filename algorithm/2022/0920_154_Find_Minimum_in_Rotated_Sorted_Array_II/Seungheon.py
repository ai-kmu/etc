# 이분탐색

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left < mid:
            # order가 안맞으면
            if nums[left] > nums[mid]:
                right = mid          
            elif nums[mid] > nums[right]:
                left = mid
            # 값이 같으면
            elif nums[mid] == nums[right] == nums[left]:
                right -= 1
                left += 1   
            # 정렬 되어있으면
            else:
                return  nums[left]
            
            mid = (left + right) // 2 
                
        return min(nums[right], nums[left])
