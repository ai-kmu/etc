class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        ans = float('inf')
        under = min(nums)
        upper = max(nums)
        k = (under + upper) // 2

        while under <= upper:
            k = (under + upper) // 2
            total = 0
            pre_total = 0
            for i, n in enumerate(nums):
                total += abs(n - k) * cost[i]
            for i, n in enumerate(nums):
                pre_total += abs(n - (k-1)) * cost[i]

            if pre_total > total:
                under = k + 1
            elif pre_total < total:
                upper = k - 1
            else:
                break
        
        return total


            
