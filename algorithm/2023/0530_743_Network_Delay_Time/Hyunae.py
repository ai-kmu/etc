# 못풀어서 답변을 참고했습니다 ㅠㅠ

import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Create adjacency list to represent the network topology
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Initialize distance array with infinity for all nodes except the source node
        distance = [float('inf')] * (n + 1)
        distance[k] = 0
        
        # Create a priority queue (min-heap) to keep track of nodes with minimum distance
        pq = [(0, k)]
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            # Ignore nodes that have already been visited with a smaller distance
            if dist > distance[node]:
                continue
            
            # Iterate through neighboring nodes and update their distances
            for neighbor, edge_weight in graph[node]:
                new_dist = dist + edge_weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        # Find the maximum distance in the distance array
        max_distance = max(distance[1:])
        
        # If any nodes have infinite distance, return -1 as signal cannot reach those nodes
        if max_distance == float('inf'):
            return -1
        
        return max_distance
