# fail code 
# t가 0인경우가 있는지 모르고 풀었어요

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # 모든 시간마다
        time = 0
        visited = set([i for i in range(1,n+1)])
        visited.remove(k)

        cur_set = set([k])

        # 그래프 만들기
        graph_dict = {}
        for s, e, t in times:
            try:
                graph_dict[s][e] = t
            except:
                graph_dict[s] = {}
                graph_dict[s][e] = t


        # 더이상 이동할 곳이 없을떄까지 반복
        while cur_set:
            print(graph_dict)
            print()
            # 시간 추가
            time += 1

            # 이전에 도착한 노드에서 갈 수 있는노드 탐색
            for s in list(cur_set):

                # 리프노드이면 제거
                if s not in graph_dict.keys():
                    cur_set.remove(s)
                    continue

                # 더이상 갈곳이 없는 노드면 제거
                if not graph_dict[s]:
                    cur_set.remove(s)
                    continue

                key_list = list(graph_dict[s].keys())
                for e in key_list:
                    graph_dict[s][e] -= 1 
                    # 도착하면
                    if graph_dict[s][e] <= 0:
                        # 현재 도달한 노드에 추가
                        cur_set.add(e)
                        # 방문처리
                        if e in visited:
                            visited.remove(e)

                        # 갈 필요 없어진 노드 제거 
                        del graph_dict[s][e]

            # 다돌았는지 확인
            if not visited:
                return time
            
        # 노드가 아직 남아있는데 이동할 수 없으면 -1 return 
        return -1
