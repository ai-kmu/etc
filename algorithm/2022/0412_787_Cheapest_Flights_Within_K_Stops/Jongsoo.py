class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #시작점에서 각 node로 가기 위한 최소 비용을 저장할 리스트
        min_cost = [float("inf")] * n
        
        #graph를 딕셔너리 형태로 바꿔서 key에는 from의 값을 value에는 튜플형태로 (to, cost)값을 저장
        #그럼 굳이 for문을 통해서 원하는 from으로 시작하는 값을 일일이 찾을 필요가 없이 graph[from]으로 to와 cost를 가져올 수 있음
        graph = collections.defaultdict(list)
        for f, t, c in flights:
            graph[f].append((t, c))
        
        #from으로 시작해서 최소비용을 갱신할 때 갖게되는 to와 cost 튜플을 저장하기 위한 deque
        q = collections.deque([(src, 0)])
        
        #k+1번을 반복하며 src부터 시작해서 갖게되는 각 node에 대한 최소 비용을 구함
        for _ in range(k+1):
            for _ in range(len(q)): #해당 차례에 가야할 경로의 수
                node, cost = q.popleft() #값을 왼쪽부터 뽑아서 해당 for문에서 가야할 경로만 뽑아옴
                for next_node, next_cost in graph[node]:
                    #현재 cost에서 next_cost를 더한 값이 next node에 대한 최소비용 값보다 작은 경우만 따져줌
                    #만약 현재 cost에서 next_cost를 더한 값이 더 크다면 이미 최소비용 값을 갖지 않으므로 신경쓸 필요가 없음
                    #최소 비용이 갱신된 경우에 다음 node로 가기 위해 next_node 값과 누적된 비용값을 q에 저장
                    if min_cost[next_node] > cost + next_cost:
                        min_cost[next_node] = cost + next_cost
                        q.append((next_node, cost + next_cost))
        
        #만약 min_cost[dst] 값이 inf라면 k+1번동안 dst node에 가지 못했다는 뜻이므로 -1을 리턴
        if min_cost[dst] == float("inf"):
            return -1
        else:
            return min_cost[dst]
