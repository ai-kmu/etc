import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            num = heapq.heappop(nums)
            heapq.heappush(nums, -num)
        return sum(nums)
