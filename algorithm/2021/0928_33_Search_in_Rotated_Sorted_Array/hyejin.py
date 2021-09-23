# binary search 문제
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]: # mid 왼쪽 부분은 정렬, 오른쪽 부분은 모름
                if target >= nums[start] and target <= nums[mid]: # 왼쪽 부분에 해당할 때
                    end = mid - 1
                else: # 오른쪽 부분에 해당할 때
                    start = mid + 1
            else: # mid 오른쪽 부분은 잘 정렬. 왼쪽 부분은 모름
                if target >= nums[mid] and target <= nums[end]: # 오른쪽 부분에 해당할 때
                    start = mid + 1
                else: # 왼쪽 부분에 해당할 때
                    end = mid - 1
        
        return -1
