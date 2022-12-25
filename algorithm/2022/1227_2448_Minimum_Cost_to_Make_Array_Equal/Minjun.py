class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        under = min(nums)
        upper = max(nums)
        k = (under + upper) // 2
        
        # trivial case
        if under == upper:
            return 0

        while under <= upper:
            k = (under + upper) // 2
            total = 0
            pre_total = 0
            for i, n in enumerate(nums):
                total += abs(n - k) * cost[i]
            for i, n in enumerate(nums):
                pre_total += abs(n - (k-1)) * cost[i]

            # 현재의 직전 값과 비교한다.
            # 직전값보다 현재가 작으면 under 땡겨온다.
            if pre_total > total:
                under = k + 1
            # 직전값보다 현재가 크면 upper 땡겨온다.
            elif pre_total < total:
                upper = k - 1
                # 직전값이 더 작으니 최신화 해준다.
                total = pre_total
            else:
                break
        return total
