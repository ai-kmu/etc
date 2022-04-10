from copy import deepcopy

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf')] * n
        cost[src] = 0
        
        # k+1번 순회
        for hop in range(k+1):
            tmp_cost = deepcopy(cost)
            # 모든 edge에 대하여 해당 edge를 통해 이동하는 것이 기존보다 cost가 낮다고 판별될 경우
            # 해당 edge를 사용한 cost로 변경
            for start, end, price in flights:
                if cost[start] + price < tmp_cost[end]:
                    tmp_cost[end] = cost[start] + price
            cost = tmp_cost
        
        return -1 if cost[dst] == float('inf') else cost[dst]
