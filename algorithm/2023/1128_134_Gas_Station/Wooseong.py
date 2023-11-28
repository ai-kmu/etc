# 키포인트
# 1. "순환"이기 때문에 해가 존재하다면 시작점은 여러 가지가 될 수 있음
#    따라서 처음부터 순차적으로 보면서 되는 곳에서 멈추면 됨
# 2. gas >= cost라면 "무조건" 해가 존재함
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        # 전체 gas가 cost보다는 많아야 해가 존재
        if total_gas < total_cost:
            return -1

        # 처음부터 시작
        curr_gas = 0
        start_pt = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            curr_gas += g - c
            
            # 만약 해당 지점으로의 이동이 딸린다면 다음 지점부터 다시 시작
            if curr_gas < 0:
                start_pt = i + 1
                curr_gas = 0

        # for문 돌고 나왔을 때의 시작 지점 반환
        return start_pt
# 1056ms, 22.2MB (12.94%)


# 키포인트: "순환"의 시작점은 minimum balance의 위치
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        # 전체 gas가 cost보다는 많아야 해가 존재
        if total_gas < total_cost:
            return -1

        total_balance = 0
        balance = []
        for g, c in zip(gas, cost):
            total_balance += g - c
            balance.append(total_balance)
        idx = balance.index(min(balance))

        return (idx + 1) % len(gas)
# 반례
# gas = [2, 0, 0, 0, 0, ...]
# cost = [0, 1, 0, 0, 0, ...]
# balance = [2, 1, 1, 1, 1, ...]
# 답 = 0
# idx = 1, 답 = 2 -> tank가 0으로 시작해서 움직일 수 없음


# 따라서 g > 0일 때만 시작점으로 삼으면?
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        # 전체 gas가 cost보다는 많아야 해가 존재
        if total_gas < total_cost:
            return -1

        total_balance = 0
        balance = []
        for g, c in zip(gas, cost):
            total_balance += g - c
            balance.append(total_balance)

        idx = balance.index(min(balance))
        # g > 0인 지점까지 계속 이동
        while gas[idx] <= 0:
            idx += 1
            if idx >= len(gas):
                idx -= len(gas)

        return (idx + 1) % len(gas)
# 반례
# gas = [7, 1, 0, 11, 4]
# cost = [5, 9, 1, 2, 5]
# 답 = 3
# balane = [2, -6, -7, 2, 1]
# idx = 2 -> 갱신 = 3 -> 답 = 4
# 하지만 그 3이 답임


# 그러면 그걸 그대로 쓰면 되긴 함.
# 근데 좀...
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        # 전체 gas가 cost보다는 많아야 해가 존재
        if total_gas < total_cost:
            return -1

        total_balance = 0
        balance = []
        for g, c in zip(gas, cost):
            total_balance += g - c
            balance.append(total_balance)

        idx = balance.index(min(balance))
        # g > 0인 지점까지 계속 이동
        flag = False
        while gas[idx] <= 0:
            flag = True
            idx += 1
            if idx >= len(gas):
                idx -= len(gas)
        # 갱신이 일어난 경우 idx 그대로 활용
        if flag:
            return idx

        return (idx + 1) % len(gas)
# 1063ms, 24.6MB (5.51%)


# two-point를 이용하면 balance를 깔끔하게 처리할 수 있음
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        # 전체 gas가 cost보다는 많아야 해가 존재
        if total_gas < total_cost:
            return -1

        balance = [g - c for g, c in zip(gas, cost)]

        n = len(balance)
        left = 0
        right = 0
        cum_balance = 0
        while left - right != n:
            if cum_balance + balance[left] >= 0:
                cum_balance += balance[left]
                left += 1
            else:
                right -= 1
                cum_balance += balance[right]

        return right if cum_balance >= 0 and right >= 0 else n + right
# 1084ms, 22.1MB (31.90%)
