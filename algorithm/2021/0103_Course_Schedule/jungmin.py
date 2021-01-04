

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)] # 노드별 연결 인덱스를 나타내는 graph 생성
    visited = [0 for _ in range(numCourses)] # 노드 방문 여부 표시 위한 리스트
    for x,y in prerequisites:
        graph[x].append(y) # 그래프 인덱스에 어떤 인덱스가 연결 되는지 작성
    for i in range(numCourses):
        if not self.dfs(graph, visited, i):
            return False # 모든 노드 탐색 안되고 한개의 노드라도 남아 있으면 false 반환
    return True # 모든 노드 탐색 완료 했으면 True 반환

def dfs(self, graph, visited, i): #깊이 우선 탐색 이용
    if visited[i] == -1: # i 인덱스를 전에 이미 방문했으면 false반환
        return False
    if visited[i] == 1:
        return True
    visited[i] = -1 # i 인덱스 방문했으면 -1로 저장
    
    for j in graph[i]: # 인덱스 i의 선수 과목 보기
        if not self.dfs(graph, visited, j):
            return False # 인덱스 i의 선수 과목을 전에 이미 방문했으면 false반환
    visited[i] = 1 
    return True
