class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 현재까지 필요한 가스 양
        required_gas = 0
        # 현재 가스 양
        curr_gas = 0
        # 현재 gas station의 위치
        start_station = 0
        for i in range(len(gas)):
            # 현재 가스를 gas - cost를 통해 구합니다.
            curr_gas += (gas[i] - cost[i])
            # 만약 현재 gas가 0보다 작다면 필요한 만큼을 required에 더해주도 현재 가스는 0으로 초기화합니다.
            if curr_gas < 0:
                required_gas -= curr_gas
                curr_gas = 0
                start_station = i + 1
        # 만약 현재 가스 양이 필요한 가스보다 많거나 같을 경우 순환이 가능한 것이므로 start_station을 반환해줍니다.
        if curr_gas >= required_gas: 
            return start_station
        # 순환이 불가능할 경우 -1을 반환해줍니다.
        return -1
