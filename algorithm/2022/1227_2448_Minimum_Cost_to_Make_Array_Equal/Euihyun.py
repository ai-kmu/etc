# 단순히 생각해서 5번째 테케에서 실패..
# 수정해보고 있어요
class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 코스트의 맥스값을 타겟으로 두고
        max_cost = cost.index(max(cost))
        min_cost = nums.index(min(nums))
        target = nums[max_cost]
        total = 0

        # 단순히 타겟이랑 맞게 계산
        for i in nums:
            start = i
            cost_num = cost[nums.index(i)]
            while True:
                if start == target:
                    break
                elif start < target :
                    start += 1
                    total += cost_num
                elif start > target :
                    start -= 1
                    total += cost_num

        return total
