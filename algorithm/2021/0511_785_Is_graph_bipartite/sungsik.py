class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # {1, -1} 두 개의 flag는 노들의 두 집합을 상징한다.
        # False일 경우 아직 접근한 적이 없다는 것을 의미한다.
        flags = [False] * len(graph)
        queue = []
        for node in range(len(graph)):
            # 아직 접근한 적이 없을 경우
            if not flags[node]:
                # 1 집합에 노드를 넣어준다.
                flags[node] = 1
                # 이후 queue에 노를 넣는다.
                queue.append(node)
            while queue:
                # queue 안에서 하나를 꺼낸다.
                node = queue.pop()
                for destNode in graph[node]:
                    # 가리키는 노드가 아직 접근한 적이 없을 경우 반대 집합에 해당 노드를 집어넣는다.
                    if not flags[destNode]:
                        flags[destNode] = -flags[node]
                        queue.append(destNode)
                        continue
                    # 만약 두 노드가 같은 집합에 있다면 bipartite가 아니므로 False를 리턴한다.
                    elif flags[destNode] == flags[node]:
                        return False
        return True