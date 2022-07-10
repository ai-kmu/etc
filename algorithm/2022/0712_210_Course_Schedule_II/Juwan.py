class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        def topo_dfs(graph, node):
            
            visited.add(node) # 방문 처리
            cycle_check.add(node) # 싸이클이 있는 지 확인하기 위해 우선 넣어줌
            for x in graph[node]: # 이웃 노드들에 대하여
                if x in cycle_check: # 만약 싸이클이라면 True를 반환
                    return True
                if x not in visited: # 아직 방문하지 않았을 때
                    if topo_dfs(graph, x): # 깊이 우선 탐색 진행
                        return True
                
                    
            cycle_check.remove(node) # 깊이 우선 탐색을 진행하여 더이상 갈 곳이 없으면
                                     # 싸이클에서 해당 노드를 지워야함. 즉, 싸이클 체크하는 것을
                                     # 초기화
            answer.append(node) # 더이상 깊게 내려가지 못할 때 그 노드를 추가.
            return False

        graph = {} # 그래프를 만들어서 그래프에서 topological sort를 DFS로 구현하여 풀이할 것임.
        
        # 그래프 빌드 시작
        for i in range(numCourses):
            graph[i] = []
            
        for edge in prerequisites:
            
            u, v = edge
            
            graph[u].append(v)
        # 그래프 빌드 종료
            
        answer = []
            
        visited = set() # DFS에서 방문 처리를 하기 위한 집합
        cycle_check  = set() # 만들어진 그래프가 DAG (Directed Asyclic Graph) 라면 필요없지만
                             # 싸이클이 있는 그래프가 테스트에 있기 때문에 싸이클을 탐지해야하는 
                             # 경우가 있음
        
        for n in graph: # 각 노드를 순회하여 DFS 탐색
            
            if n not in visited:
                
                if topo_dfs(graph, n):
                    return []
                
        return answer
    
    
