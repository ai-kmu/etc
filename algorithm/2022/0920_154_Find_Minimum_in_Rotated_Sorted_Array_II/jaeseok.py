class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums를 순차탐색하면서 첫 번째 숫자보다 작아지는 숫자가 있으면 그 숫자가 최솟값이 됨.
        for i in nums:
            if nums[0] > i:
                return i
        # 그런 숫자가 존재하지 않으면 nums는 rotation이 일어나지 않음.
        return nums[0]
      
