class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # binary search를 활용한 풀이
        def getCost(target):
            tmp_cost = 0
            for i, num in enumerate(nums):
                tmp_cost += cost[i] * abs(target - num)
            return tmp_cost

        # 가능한 숫자 중 최소와 최대는 nums의 최솟값과 최댓값
        l, r = min(nums), max(nums)
        m = (l + r) // 2
        m_cost = getCost(m)
        while l <= r:
            m = (l + r) // 2
            # l과 r 중간의 값과 그보다 1 작거나 큰 값에 대해 cost를 계산한다
            m_cost = getCost(m)
            ml_cost = getCost(m-1)
            mr_cost = getCost(m+1)
            # 만약 1 작은 값이 cost가 더 작을 경우
            # r을 m 왼쪽으로 이동
            if m_cost > ml_cost:
                r = m - 1
            # 만약 1 큰 값이 cost가 더 작을 경우
            # l을 m 오른쪽으로 이동
            elif m_cost > mr_cost:
                l = m + 1
            # m 위치에서 모두 작을 경우 m에서 최솟값을 가짐
            else:
                break

        return m_cost

