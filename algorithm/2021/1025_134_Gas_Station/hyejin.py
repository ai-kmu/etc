class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # O(n^2)은 time limit
        nums = len(gas)
        
        # 조건 1. 오른쪽 sum + 왼쪽 sum이 >=0 이어야함. 일단 sum이 <0이면 그냥 불가능한거임.
        # 오른쪽부분 먼저 +로 유지되는 지점을 N번 돌아 찾고, 왼쪽을 검증
        sum_gas = 0
        start_idx = 0
        for i in range(nums):
            sum_gas += gas[i] - cost[i]
            if sum_gas < 0:
                start_idx = i+1
                sum_gas = 0

        if start_idx > nums - 1:
            return -1
        
        # 오른쪽은 유지되고 start_idx의 왼쪽부분도 +가 유지되는지 검증
        for i in range(start_idx):
            sum_gas += gas[i] -cost[i]
            if sum_gas < 0:
                return -1
        
        return start_idx
