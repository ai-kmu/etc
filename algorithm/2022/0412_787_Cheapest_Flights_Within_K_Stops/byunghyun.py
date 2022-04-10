class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        max_count = K + 1
        graph = collections.defaultdict(dict)
        for flight in flights:
            graph[flight[0]][flight[1]] = flight[2] # defaultdict을 이용하여 그래프를 만들어준다.
        queue = collections.deque() # 일반 리스트로 하면 시간초과가 떠서 deque를 이용하여 주었다.
        queue.append((0, src, max_count)) # 순서대로 비용, 출발점, 남은 카운트가 된다.
        cost_map = [float("inf") for _ in range(n)] # 처음에 cost_map은 무한으로 요소를 채워준다.
        
        while len(queue) > 0: # 남은 큐가 0이 될 때까지 BFS로 탐색
            tmp_ele = queue.popleft() # 제일 오래된 요소부터 꺼내준다.
            cost = tmp_ele[0] # 누적된 비용
            cur_src = tmp_ele[1] # 현재 출발하는 지점
            count = tmp_ele[2] # 남은 카운트
            if count > 0:
                for candidate in graph[cur_src]: # 그래프를 이용하여 이동 가능한 후보들을 선출한다. 
                    tmp_cost = cost + graph[cur_src][candidate] # 해당 후보지를 거치는 것이
                    if tmp_cost < cost_map[candidate]: # 더 가까운 거리가 된다면
                        cost_map[candidate] = tmp_cost # cost_map 업데이트
                        queue.append((tmp_cost, candidate, count-1)) #큐에 요소추가
                        
                        
        if cost_map[dst] == float("inf"): # 만약 cost_map에서 목적지로의 거리가 계속 무한으로 남아있다면
            return -1 # 갈수 없음
        else:
            return cost_map[dst] #최소 거리를 반환
            
                    
            
            
