# import numpy as np
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # lst = np.array(matrix).flatten().tolist()
        hq = []
        # for i in lst:
        for i in matrix:
            for j in i:
                heapq.heappush(hq, j)
        
        answer = 0
        for i in range(k):
            answer = heappop(hq)

        return answer
