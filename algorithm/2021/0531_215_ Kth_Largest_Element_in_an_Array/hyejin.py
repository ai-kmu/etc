class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nlogn
        sort_nums = sorted(nums)[::-1] # reverse sort
        return sort_nums[k-1] # k-1번째 추출
