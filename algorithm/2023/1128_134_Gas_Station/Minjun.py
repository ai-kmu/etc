class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 실패
        if sum(gas) < sum(cost):
            return -1
        # 성공의 경우 (optimal)
        idx = 0
        tank = 0
        for i, g in enumerate(gas):
            # 누적합
            tank += g - cost[i]
            # optimal하기 때문에 실패하면, 다음 지점부터 다시 시작
            if tank < 0:
                idx = i+1
                tank = 0
        return idx

