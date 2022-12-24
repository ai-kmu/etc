'''
가능한 nums의 범위 안에서 binary search를 이용해 cost가 감소하는 방향으로 탐색
'''
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def get_cost(num):
            result = 0
            for i in range(len(nums)):
                result += abs(nums[i]-num) * cost[i]
        
            return result

        l = min(nums)
        h = max(nums)

        while l <= h:
            m = (l+h) // 2
            
            # m일때 cost보다 m-1일때 cost가 작다 -> 왼쪽 덩어리 탐색
            # m일때 cost보다 m+1일때 cost가 작다 -> 오른쪽 덩어리 탐색
            if get_cost(m-1) < get_cost(m):
                h = m - 1
            else:
                l = m + 1
                
        return min(get_cost(m), get_cost(l), get_cost(h))
