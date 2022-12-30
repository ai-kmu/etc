import heapq

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # O(k * n)으로 풀면 time error
        # 최댓값을 유지해가며 만약 최댓값이 window에서 벗어날 경우 그 다음 최댓값을 알아야 함
        # 따라서 heap을 이용하여 최댓값을 유지하되 window에서 벗어날 경우 heappop을 수행
        heap = []
        heapq.heappush(heap, (-nums[0], 0))

        for i, num in enumerate(nums[1:n-1], 1):
            while heap[0][1] + k < i:
                heapq.heappop(heap)
            heapq.heappush(heap, (-num + heap[0][0], i))
        
        # 최댓값이 아닌 마지막에서의 값을 구하고 싶으므로
        # 마지막은 heappush를 하지 않고 heappop만 하고
        # 최댓값과 nums의 마지막 값을 더한 값을 Return
        while heap[0][1] + k < n-1:
            heapq.heappop(heap)
        
        return -heap[0][0] + nums[-1]
