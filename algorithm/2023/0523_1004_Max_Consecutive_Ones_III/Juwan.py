from collections import deque

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        my_q = deque()

        start, end, max_cnt = 0, 0, 0

        for idx, i in enumerate(nums):
            if i == 0:
                my_q.append(idx)
            
            if len(my_q) > k:
                cnt = end - start

                max_cnt = max(max_cnt, cnt)

                start = my_q.popleft() + 1

            end += 1

        cnt = end - start

        return max(max_cnt, cnt)
