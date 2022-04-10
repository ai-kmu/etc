import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        route = [[] for i in range(n)]
        
        # 인접 리스트 생성
        for i, j, k_ in flights:
            route[i].append((j, k_))
        
        visited = {}
        # heap 초기화 -> (가격, 몇 번 stop을 거쳤는지, 도착지)
        heap = [(0, -1, src)]
        
        while heap:
            cost, k_cnt, curr = heapq.heappop(heap) # 가장 cost가 작은 node를 pop
            
            # pop한 node의 현재 위치가 도착지(dst) 라면 return
            if curr == dst: return cost
            
            # 현재 node(curr) 가 아직 방문하지 않았고, k_cnt 보다 큰 경우
            if curr not in visited.keys() or visited[curr] > k_cnt:
                visited[curr] = k_cnt # 방문했다고 표기
                if k_cnt < k:
                    for end, price in route[curr]:
                        # heap에 cost를 갱신, k_cnt 를 1만큼 증가
                        heapq.heappush(heap, (cost + price, k_cnt + 1, end))
            # print(visited)
        return -1
