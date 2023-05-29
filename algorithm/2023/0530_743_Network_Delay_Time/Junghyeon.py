'''
다익스트라를 사용하여 거리정보를 업데이트 하고 그 중 최댓값을 리턴
'''
import heapq


class Solution:    
    def networkDelayTime(self, times, n, k):
        # times[i] = (ui, vi, wi)의 형식 -> 이를 바탕으로 graph 생성
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        
        # heapq 초기화
        que = [(0, k)]

        while que:
            time, node = heapq.heappop(que)

            if time > dist[node]:
                continue

            for dest, cost in graph[node]:
                new_time = time + cost
                # 거리정보 업데이트
                if new_time < dist[dest]:
                    dist[dest] = new_time
                    heapq.heappush(que, (new_time, dest))
        
        print(dist)

        dist[0] = -1
        
        # 끊어진 노드가 있으면 -1을 리턴
        if max(dist) == float('inf'):
            return -1
    
        else:
            return max(dist)
