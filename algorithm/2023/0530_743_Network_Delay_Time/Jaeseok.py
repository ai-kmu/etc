import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 다익스트라 알고리즘으로 해결
        graph = {i: [] for i in range(1, n + 1)}
        # 각 그래프 연결과 거리를 딕셔너리에 저장
        for u, v, w in times:
            graph[u].append((v, w))

        # 최대 거리(6000 * 100)로 distance 딕셔너리 초기화
        distance = {i: 600000 for i in range(1, n + 1)}
        distance[k] = 0

        # 시작 노드로부터 heap 초기화, 첫번째는 소요시간, 두번째는 노드 번호를 의미
        h = [(0, k)]
        while h:
            # 힙에서 가장 시간(같으면 노드)이 적게 걸리는 것부터 뽑아냄
            time, node = heapq.heappop(h)
            # 소요 시간이 현재 distance에 있는 node보다 더 많이 걸리면 배제
            if time > distance[node]:
                continue
            # 현재 노드에서 연결된 그래프를 전부 확인하면서
            for n_node, n_time in graph[node]:
                next_time = time + n_time
                # 이 노드에서 가장 적게 걸리는 시간이 있으면 저장하고 힙에 추가
                if next_time < distance[n_node]:
                    distance[n_node] = next_time
                    heapq.heappush(h, (next_time, n_node))

        answer = max(distance.values())
        # 최대거리가 초기값 : 한번도 방문하지 못한 노드가 존재하므로 -1 리턴
        if answer == 600000:
            return -1
        else:
            return answer
