# 흠 오랜만에 다익스트라 푸니까 못풀겠네요... 솔루션 봤습니다.
# 그래서 리뷰는 괜찮아요!

import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        # 그래프 초기화
        # 인접 리스트로 그래프 표현
        graph = [[] for _ in range(n+1)]  
        for u, v, w in times:
            # u에서 v로 가는 간선의 정보 저장
            graph[u].append((v, w))  
        # 최단 거리 초기화
        dist = [float('inf')] * (n+1) 

         # 출발 노드의 최단 거리 0
        dist[k] = 0 

        # 우선순위 큐 초기화
        # (거리, 노드) 쌍을 저장하는 우선순위 큐
        pq = [(0, k)] 

        while pq:
            # 우선순위 큐에서 가장 작은 거리를 가지는 노드 선택
            d, node = heapq.heappop(pq)  

            # 이미 처리된 노드 스킵
            if d > dist[node]:
                continue

            # 인접 노드 순회
            for neighbor, delay in graph[node]:
                # 현재 노드를 거쳐 인접 노드로 가는 거리 계산
                new_dist = d + delay  
                # 더 짧은 거리를 찾은 경우
                if new_dist < dist[neighbor]:
                    # 최단 거리 업데이트
                    # 우선순위 큐에 삽입
                    dist[neighbor] = new_dist  
                    heapq.heappush(pq, (new_dist, neighbor))  

        # 모든 노드의 최단 거리 중 가장 큰 값을 찾음
        max_delay = max(dist[1:])  

        # 모든 노드에 도달할 수 없는 경우 0 아님 max리턴
        if max_delay == float('inf'):  
            return -1
        else:
            return max_delay  
