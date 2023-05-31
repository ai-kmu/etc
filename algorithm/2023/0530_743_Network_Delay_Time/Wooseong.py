import heapq as hq
from collections import defaultdict as ddict

# djisktra
class Solution(object):
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # times 변수 dictionary로 인접 행렬처럼 만들기
        adj = ddict(list)
        for u, v, w in times:
            adj[u].append((w, v))
        
        # 방문 체크
        visited = set()

        # heap을 이용해서 걸린 시간 정렬
        heap = [(0, k)]
        while heap:
            total, node = hq.heappop(heap)
            visited.add(node)

            # 모든 곳을 방문 했으면 그 때의 total이 정답
            if len(visited) == n:
                return total
            
            # 해당 노드의 이웃 노드 탐색
            for w, v in adj[node]:
                if v not in visited:
                    hq.heappush(heap, (total + w, v))
        
        return -1
