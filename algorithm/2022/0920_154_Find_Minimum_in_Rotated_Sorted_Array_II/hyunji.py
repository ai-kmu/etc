# heap 사용 - 54ms, 14.5MB
import heapq

class Solution:
    def findMin(self, nums: List[int]) -> int:
        heapify(nums)
        
        return nums[0]

      
# 순차적으로 배열을 탐색했을 때, 배열의 첫번째 element보다 작은 첫번째 값은 rotation의 시작점
# 119ms, 14.4MB
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        num = nums[0]
        
        for n in nums:
            if n < num:
                return n
            
        return num
