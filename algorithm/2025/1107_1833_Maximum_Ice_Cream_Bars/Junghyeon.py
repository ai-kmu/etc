from collections import heapq

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        heapq.heapify(costs)
      
        while costs:
            coins -= costs[0]
            if coins < 0:
                return ans
            ans += 1
            heapq.heappop(costs)
          
        return ans
