class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        
        # 이동횟수-1이 K번에 도달할때까지 dst에 도착하는 최소비용을 찾는방식
        
        # 출발지와 목적지에따른 cost를 불러 올 수 있게 defaultdict사용
        flights_cost_list = defaultdict(dict)
        for departure_node, dst_node, cost in flights:
            flights_cost_list[departure_node][dst_node] = cost

        # 최솟값 테이블
        min_cost_table = [float('inf')] * n
        
        # 현재노드, 이동횟수, 현재 노드까지의 비용
        que = deque([(src, 0, 0)])

        # que의 값이 없을때까지 반복
        while que:   
            # 현재 노드에대한 정보를 pop
            cur_node, move_count, cost = que.popleft()
            
            # 현재 노드가 목적지에 도달하였거나, K번이동했으면 이번 노드 무시
            if cur_node == dst or move_count - 1 == K:
                continue 
            
            # 현재 노드에서 이동할 수 있는노드
            for next_node in flights_cost_list[cur_node].keys():
                
                # 현재 노드에서 이동할 수 있는노드까지의 비용
                cur_cost =  flights_cost_list[cur_node][next_node]
                
                # 현재노드에서 다음 노드까지의 비용이 다음노드의 최소비용보다 커지면 이번 노드 무시
                if cost + cur_cost >= min_cost_table[next_node]:
                    continue
                    
                # min_cost_table 에 최소비용 update
                min_cost_table[next_node] = min(min_cost_table[next_node], cost + cur_cost)
                
                # que에 next_node append
                que.append([next_node, move_count + 1, cost + cur_cost])

        return min_cost_table[dst] if min_cost_table[dst] < float('inf') else -1
