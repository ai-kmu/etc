import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # heap을 활용한 풀이
        visited = set()
        heap = [(0, k)]
        answer = -1
        
        while heap:
            # 현재 가능한 가장 작은 path를 구함
            min_weight, min_node = heapq.heappop(heap)
            # 만약 방문하지 않은 node라면 해당 path가 그 node로 가는 최솟값
            if min_node in visited:
                continue
            visited.add(min_node)
            answer = max(answer, min_weight)
            
            # 방문함으로써 가능해진 path들을 추가
            for start, end, weight in times:
                if min_node == start and end not in visited:
                    heapq.heappush(heap, (weight + min_weight, end))
        
        
        return -1 if len(visited) != n else answer
        
