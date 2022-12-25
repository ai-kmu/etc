class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # 주어진 숫자(compare)로 맞추는 데 드는 cost를 계산하는 함수
        def cal_cost(compare):
            costs = 0
            for n, c in zip(nums, cost):
                costs += abs(n - compare) * c
            return costs

        # left: 최소 / right: 최대
        left = min(nums)
        right = max(nums)
        # binary search
        # left == right면 while 스킵 (예외 처리)
        while left < right:
            mid = (left + right) // 2
            # 조금 다르게, 중간이랑 그 다음 값을 비교해서
            sum_mid = cal_cost(mid)
            sum_next = cal_cost(mid + 1)
            
            # 중간이 작으면 right를 당기고
            if sum_mid < sum_next:
                right = mid
            # 중간이 크면 left를 그 다음으로 넘김
            else:
                left = mid + 1
        
        # 답은 left로
        return cal_cost(left)
