# 틀린 코드, cycle 처리 필요함

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 그래프를 dictionary를 통해 생성한다.
        graph = {c:[] for c in range(4)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        # 재귀가 끝나면 저장하는 output list와 방문 노드를 저장하는 visit list를 만든다.
        output = []
        visit = []

        def dfs(node, visit, output):
            # 먼저 node를 visit list에 저장한다.
            visit.append(node)
            # 그 뒤에 node의 인접 노드를 재귀를 통해 탐색하면서 visit 갱신한다.
            for nx in graph[node]:
                if nx not in visit:
                    dfs(nx, visit, output)
            # 뿌리 node까지 가게 되면 output에 추가한다.
            output.append(node)

        for i in range(numCourses):
            if i not in visit:
                dfs(i, visit, output)
                
        return output
