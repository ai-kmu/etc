class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        def f(x): # x값으로 모든 숫자를 바꿨을 때의 비용 총합
            res = 0
            for i in range(len(nums)):
                res += abs(nums[i] - x) * cost[i]
            return res

        lo = min(nums) - 1
        hi = max(nums) + 1

        while hi - lo > 1:
            m = (lo + hi) >> 2 # 비트 연산. 반으로 나눈 값과 동일함
            
            if f(m) <= f(m + 1):
                hi = m
            else:
                lo = m + 1
                
        return min(f(lo), f(hi))
      # 시간 초과 뜸..
