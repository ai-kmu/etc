import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        res = matrix[0] 
        heapq.heapify(res) # 가장 첫번째 행을 힙 구조로 만들고

        for r in matrix[1:]:
            for i in r:
                heapq.heappush(res, i) # 만든 힙 구조에 하나씩 넣으면 자동으로 힙구조로 정렬 되어있을 것임


        return heapq.nsmallest(k, res)[-1] # heapq의 펑션을 이용하면 쉽게 
        
