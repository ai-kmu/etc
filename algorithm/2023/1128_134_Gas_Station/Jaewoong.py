class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # start_station: 출발 스테이션의 인덱스(0으로 설정)
        # total_gas: 전체 여행동안의 가스 잔량
        start_station = 0
        total_gas, current_gas = 0, 0
        
        # gas 소모 계산(3번 station에서 시작하면 4 - 1)
        # 현재 가스를 계산하는 이유는 음수 즉, 출발이 불가한 경우를 상정, 그러면 다음 station에서 시도
        for i in range(n):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            
            # 다음 station에 도착 못하면
            if current_gas < 0:
                current_gas = 0
                start_station = i + 1
        
        # total_gas가 0보다 크면 가능
        if total_gas >= 0:
            return start_station
        else:
            return -1
