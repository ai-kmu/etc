import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for i in range(n)]
        
        # 그래프에 각 비행 정보 저장
        for i, j, c in flights:
            graph[i].append((j, c))
        
        # 아직 방문하지 않은 곳만 가야함
        visited = {}
        q = []
        # 순서대로 (가격, 몇번째 stop인지, 도착지)를 의미
        heapq.heappush(q, (0, -1, src))
        
        while q:
            cost, n, cur_city = heapq.heappop(q)
            if cur_city == dst:
                return cost
            # 아직 방문한적 없고 k보다는 작지만 n보다는 큰 경우
            if cur_city not in visited.keys() or visited[cur_city] > n:
                visited[cur_city] = n
                if n < k:
                    for end, price in graph[cur_city]:
                        heapq.heappush(q, (cost + price, n + 1, end))

        return -1