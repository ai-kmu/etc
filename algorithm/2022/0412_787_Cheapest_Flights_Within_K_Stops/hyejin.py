class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # n개의 city가 있다.
        # flight로 연결됨 flight[i] = [from, to, price]
        # src, dst, 최대 k번 stop
        # the cheapest price
        
        # paths / 일반 list는 시간초과
        paths = collections.defaultdict(list)
        for s, e, price in flights:
            paths[s].append((e, price))
        
        costs = [float("inf") for _ in range(n)]
        
        num = -1 
        q = [(src, 0)] # 처음은 src에서 시작, before_cost는 0
        while 0 < len(q) and num < k:
            num += 1
            new_q = []
            for s, before_cost in q: # stop의 횟수가 같은 노드들은 한번에 계산
                for e, price in paths[s]: # s- e의 간선 cost 계산
                    # memory 차지함, 작지 않으면 굳이 들를 필요가 없음
                    # costs[e] = min(costs[e], before_cost + price)
                    # q.append((e, costs[e]))
                    if before_cost + price < costs[e]: 
                        costs[e] = before_cost + price
                        new_q.append((e, costs[e]))
            q = new_q
        return -1 if costs[dst] == float('inf') else costs[dst]
