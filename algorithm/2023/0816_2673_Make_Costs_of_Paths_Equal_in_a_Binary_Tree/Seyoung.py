from typing import List

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        total_increments = 0
        
        for i in range(n - 1, 0, -1):
            left_child = 2 * i
            right_child = 2 * i + 1
            
            cost_diff = abs(cost[left_child - 1] - cost[right_child - 1])
            
            if cost[left_child - 1] < cost[right_child - 1]:
                cost[left_child - 1] += cost_diff
                total_increments += cost_diff
            else:
                cost[right_child - 1] += cost_diff
                total_increments += cost_diff
        
        return total_increments
