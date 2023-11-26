# fail code
# O(n^2) 으로 풀었는데 O(n)으로 풀어야 할 듯

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        len_travel = len(gas)
        for start_point in range(len_travel):
            cur_gas = gas[start_point]
            for i in range(len_travel+1):
                next_point = (start_point + i + 1)%len_travel
                cur_point = (start_point + i)%len_travel
                next_gas = gas[next_point]
                needed_cost = cost[cur_point]
                
                if cur_gas - needed_cost < 0:
                    break
                else:
                    cur_gas = cur_gas - needed_cost + next_gas

                if i == len_travel:
                    return start_point

        return -1
