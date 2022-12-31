'''
DP[i] = max(DP[i-1], DP[i-2], ..., DP[i-k+1]) + nums[i]
-> max를 위해 for문을 돌면 TLE
-> heap을 이용해서 볼 수 있는 범위에서 최댓값 저장
'''

import heapq as hq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # DP: 범위보다 작은 값으로 초기화, 첫번째는 주어진 nums의 첫 값과 같음
        DP = [-16383 for _ in nums]
        DP[0] = nums[0]

        # 최댓값을 저장하는 heap
        # 최댓값, 그 값의 index의 튜플로 저장
        heap = [(-nums[0], 0)]
        for i in range(1, len(nums)):
            max_, ind = heap[0]
            # 값의 index가 볼 수 있는 범위를 벗어났다면 pop
            while ind < i - k:
                hq.heappop(heap)
                max_, ind = heap[0]

            # 최댓값 + 현재 nums
            DP[i] = -max_ + nums[i]
            # heap 업데이트
            hq.heappush(heap, (-DP[i], i))
        
        # 답은 마지막에
        return DP[-1]
