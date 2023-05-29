# DFS 풀이
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, n, k):
        # 그래프 생성
        graph = defaultdict(list)
        for u, v , w in times:
            graph[u].append((w,v))

        # 거리 초기화
        distances = {node: float('inf') for node in range(1,n+1)}

        # 노드 탐색
        def dfs(node, current_time):
            # 경과 시간이 노드의 최단 경로 보다 크거나 같으면 종료
            if current_time >= distances[node]: 
                return 
            # dist 업데이트
            distances[node] = current_time
            # 모든 인접 노드에 대해 재귀적으로 호출
            for time, neighbor in sorted(graph[node]):
                dfs(neighbor, current_time + time)
        dfs(k, 0)
        # distances값 중 가장 큰 값 반환(무한대 예외 처리)
        ans = max(distances.values())
        if ans < float('inf'):
            return ans  
        else:
            return -1
