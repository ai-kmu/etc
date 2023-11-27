# 1트 - 시간 초과뜸 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n개의 가스 station. gas[i]는 i번째에 gas[i]만큼의 가스가 있다는 것을 의미함
        # cost[i]는 i에서 i+1까지 이동할 때 소요되는 가스량을 의미함
        ans = -1
        sub = deque()
        start_indices = []

        for idx, (x, y) in enumerate(zip(gas, cost)):
            sub.append(x - y)
            if x - y >= 0:
                start_indices.append(idx)

        for i in start_indices:
            sub.rotate(len(sub) - i)
            cnt = 0
            for j in sub:
                cnt += j
                if cnt < 0:
                    break
            if cnt >= 0:                    
                ans = i
            sub.rotate(len(sub)+i)

        return ans


# 2트
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n개의 가스 station. gas[i]는 i번째에 gas[i]만큼의 가스가 있다는 것을 의미함
        # cost[i]는 i에서 i+1까지 이동할 때 소요되는 가스량을 의미함

        total_gas = 0
        total_cost = 0
        sub = []

        for i in range(len(gas)):
            sub.append(gas[i] - cost[i]) # 충전 가능한 가스량 - 사용 예정 가스량을 담은 리스트
            total_gas += gas[i]
            total_cost += cost[i]

        if total_gas < total_cost: # 어차피 돌아오지 못하면 return -1
            return -1

        start = 0
        current_gas = 0

        for i in range(len(sub)):
            current_gas += sub[i]

            if current_gas < 0: # 만약 current_gas가 0보다 작으면, 순환 불가.
                start = i + 1 # 인덱스를 옮기고, 위 과정 반복
                current_gas = 0

        return start % len(gas)
