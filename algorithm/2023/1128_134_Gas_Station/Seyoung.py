from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        total_gas, current_gas, station = 0, 0, 0

        for i in range(n):
            # 총 가스와 현재 가스를 여행비용 계산해서 누적계산
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            # 남은 가스가 없으면 다음 주유소로~
            if current_gas < 0:
                current_gas = 0
                station = i + 1

        # 총 가스가 없으면 주행 불가능 => -1 
        if total_gas < 0:
            return -1
        else:
            return start_station % n
