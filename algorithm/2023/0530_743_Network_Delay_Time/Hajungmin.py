import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # initialize table
        # table을 딕셔너리 형태로 변환
        new_times = dict()
        for s, e, w in times:
            if s not in new_times.keys():
                new_times[s] = {e:w}
            else:
                new_times[s][e] = w

        # 각 노드 별 거리 값을 저장할 distance 만들기
        distances = [1000 for _ in range(n)]

        # 처음 탐색할 노드의 거리와 노드를 넣어줌
        # 시작 노드이기 때문에 거리는 0
        queue = []
        heapq.heappush(queue, [0, k])

        # 큐 안에 값이 존재한다면 해당 노드의 거리와 노드를 가져옴
        while queue:
            curr_distance, curr_node = heapq.heappop(queue)

            # 만약 해당 노드의 계산된 거리가 현재 큐에서 가져온 거리보다 작으면
            # 볼 필요가 없기 때문에 continue
            if distances[curr_node-1] < curr_distance:
                continue
            
            # 만약 딕셔너리 키 값에 현재 큐에서 나온 노드가 없다면 
            # 해당 노드는 자식 노드가 없는 부모 노드이기 때문에 continue
            if curr_node not in new_times.keys():
                continue

            # 딕셔너리에서 현재 큐에서 나온 노드에서부터 자식 노드들을 뽑아서 거리를 계산하고
            # 업데이트 시킴
            for new_node, new_distance in new_times[curr_node].items():
                distance = curr_distance + new_distance
                # 만약 계산된 거리가 현재 기록된 거리보다 작을 경우 
                # 거리 값을 업데이트하고 큐에 새로운 거리와 노드를 넣어줌
                if distance < distances[new_node-1]:
                    distances[new_node-1] = distance
                    heapq.heappush(queue, [distance, new_node])

        # 현재 노드에 해당하는 거리를 제외한 거리 값들 중 가장 큰 값을 정답 값으로 선택
        answer = max(distances[:k-1]+distances[k:])
        return answer if answer != 1000 else -1
