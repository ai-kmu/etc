# 다익스트라 알고리즘 풀이
# 다익스트라 까먹어서 인터넷에서 다익스트라 알고리즘 코드 참고 하였음

from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        g = defaultdict(list)

        dict_w = {}
        distance = []

        for u, v, w in times:
            g[u].append((w, v))

        q, visited, res = [], {}, []

        heappush(q, (0, k))

        while q:
            weight, node = heappop(q)
            if node not in visited:
                visited[node] = weight
                for next_w, next_node in g[node]:
                    heappush(q, (weight + next_w, next_node))

        return list(visited.values())[len(visited)-1] if len(visited) == n else -1
