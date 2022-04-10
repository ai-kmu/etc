class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K:int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])
        k = 0
        visit = {}
        Q = [(0, src, 0)]
        
        while Q:
            price, node, k = heapq.heappop(Q)  # 비용, 노드, 갈 수 있는 경유지 수
            if node == dst:  # 도착한 경우
                return price  # return price(비용)
            
            if node not in visit or visit[node] > k:  # 방문하지 않았거나, 경유지 할당 수를 넘은 경우
                visit[node] = k
                for v, w in graph[node]:  # 노드, 이동비용
                    if k <= K:
                        result = price + w  # 이동비용 + 현재 비용
                        heapq.heappush(Q, (result, v, k + 1))
        return -1
