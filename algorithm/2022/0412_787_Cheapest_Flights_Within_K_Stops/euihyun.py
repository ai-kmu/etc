import collections
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # graph 인접 리스트 생성
        graph = collections.defaultdict(list)
        for from_node, to_node, p in flights:
            graph[from_node].append((to_node, p))  # (graph[from] 에서 to와 price 의 형태)

        q = [(0, src, k)]  # 비용(0으로 초기화), 출발 정점, 남은 경유지

        while q:
            price, node, k = heapq.heappop(q)  # 가격, 정점, 경유지 할당
            if node == dst:  # 도착하면 price 리턴
                return price

            if k >= 0:  # 경유지가 0이상 일 경우
                for v, w in graph[node]:  # v 에 노드, w에 이동비용 할당
                    total = price + w  # 이동비용 현재비용 합
                    heapq.heappush(q, (total, v, k - 1))  # 다시 heappush

        return -1  # k가 음수인 상태에서 dst에 도착하지 못하면 -1 리턴