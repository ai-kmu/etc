# 답 보고 풀었습니다.
# 풀이 안해주셔도 되요

# 다 익스트라 알고리즘을 이용하여 최소값을 찾는 코드

import heapq


class Solution:
    def networkDelayTime(self, times, n, k):
        # Initialize graph and distance
        graph = [[] for _ in range(n + 1)]

        dist = [-1] + [float('inf')] * (n)
        dist[k] = 0
        
        for u, v, w in times:
            graph[u].append((w, v))
        
        heap = [(0, k)]
        
        # Dijkstra
        while heap:
            d, node = heapq.heappop(heap)
            if d <= dist[node]:
                for w_next, node_next in graph[node]:
                    d_next = d + w_next
                    if d_next < dist[node_next]:
                        dist[node_next] = d_next
                        heapq.heappush(heap, (d_next, node_next))
        
        # Get max delay
        max_delay = max(dist)
                
