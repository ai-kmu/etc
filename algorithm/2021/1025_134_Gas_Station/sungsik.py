class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas와 cost의 차이를 통해 해당 station을 가는데 얼만큼의 cost가 드는지 확인
        diff = [x-y for x, y in zip(gas, cost)]
        # circular이기 때문에 2만큼 곱함
        diff *= 2
        distance = len(gas)
        
        # 초기 시작값과 가스 잔여량을 0으로 설정
        start = 0
        gas_tank = 0
        for end in range(len(diff)):
            # gas tank에 gas와 cost의 차이를 더함
            gas_tank += diff[end]
            # 만약 가스 잔여량이 0보다 적을 경우 해당 구간은 갈 수 없다고 판단
            if gas_tank < 0:
                # 가스 잔여량을 0으로 설정하고 시작점을 끝점 바로 다음으로 초기화해서
                # 이전 구간은 버림
                gas_tank = 0
                start = end+1
                # 만약 시작점이 가능한 구간을 벗어난 경우 -1을 출력
                if  start > distance:
                    return -1

            # 가스 잔여량이 0보다 같거나 많을 경우
            else:
                # 끝점과 시작점의 차이가 distance보다 클 경우
                # 시작점을 출력
                # 시작점이 유일함을 보장하기 때문에 발견했을 때 바로 출력해보 문제가 없다
                if end - start >= distance:
                    return start
                
        return start
