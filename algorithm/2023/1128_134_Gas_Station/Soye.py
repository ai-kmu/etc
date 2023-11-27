from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 만약 총 가스량이 총 비용보다 작다면 -1 반환
        if sum(gas) < sum(cost):
            return -1

        current_tank, start_idx, num_stations = 0, 0, len(gas)
        for station in range(num_stations):
            current_tank += gas[station] - cost[station]
            # 현재 탱크가 음수일 경우, 시작 주유소를 다음 주유소로 갱신하고 현재 탱크를 0으로 초기화
            if current_tank < 0:
                start_idx = station + 1
                current_tank = 0 
        
        # 시작 주유소 인덱스 반환
        return start_idx
