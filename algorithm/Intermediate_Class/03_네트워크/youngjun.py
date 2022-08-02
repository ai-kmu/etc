# Sol 1) BFS

from collections import deque

def bfs(n, graph, visited):
    # queue 초기화한다.
    queue = deque()
    # queue에 초기 노드를 넣는다.
    queue.append(n)

    # queue가 없어질 때 까지
    while queue:
        # queue의 원소를 popleft하고 node를 초기화한다.
        node = queue.popleft()
        # 만약 아직 탐색하지 않은 노드라면
        if visited[node] == 0:
            # 탐색한 것을 표시하고
            visited[node] = 1
            # 노드의 인접 노드를 탐색하여
            for i in graph[node]:
                # queue에 넣어준다.
                queue.append(i)

    # visited를 반환한다.
    return visited   

def solution(n, computers):
    # answer를 0으로 초기화한다.
    answer = 0
    # computers 그래프의 인접 해시 테이블을 초기화한다.
    graph = {node:[] for node in range(n)}
    # visited list를 초기화한다.
    visited = [0]*n 
    
    # computers 그래프의 인접 해시 테이블을 생성한다.
    for i in range(n):
        for j in range(n):
            # 노드가 서로 연결되어 있거나, 자기 자신이 아닐 경우
            if computers[i][j] == 1 and i != j:
                # 인접 해시테이블에 추가한다.
                graph[i].append(j)

    # n번 순회하면서
    for i in range(n):
        # 만약 visited list에 0이 남아있다면
        if 0 in visited:
            # 0이 남아있는 위치를 f_node로 설정해 준 이후
            f_node = visited.index(0)
            # f_node가 i와 같다면
            if f_node == i:
                # bfs를 통해 한 노드에 직접, 간접적으로 연결되어 있는 노드 탐색한다.
                bfs(f_node, graph, visited)
                # 탐색 이후 answer에 1을 더해준다.
                answer += 1
            # f_node가 i와 같지 않다면
            else:
                # 그냥 넘어간다.
                continue

    # answer를 반환한다.
    return answer

# Sol 2) DFS

def dfs(n, graph, visited):
    # 만약 node가 이미 탐색이 끝났다면
    if visited[n] == 1:
        # visited를 반환한다.
        return visited
    # 만약 node가 탐색되지 않았다면 (visited[n] == 0)
    else:
        # 탐색한 것을 표시하고
        visited[n] = 1
        # graph의 node들을 순회하면서
        for node in graph[n]:
            # 재귀를 통해 탐색한다.
            dfs(node, graph, visited)

def solution(n, computers):
    # answer를 0으로 초기화한다.
    answer = 0
    # computers 그래프의 인접 해시 테이블을 초기화한다.
    graph = {node:[] for node in range(n)}
    # visited list를 초기화한다.
    visited = [0]*n 
    
    # computers 그래프의 인접 해시 테이블을 생성한다.
    for i in range(n):
        for j in range(n):
            # 노드가 서로 연결되어 있거나, 자기 자신이 아닐 경우
            if computers[i][j] == 1 and i != j:
                # 인접 해시테이블에 추가한다.
                graph[i].append(j)

    # n번 순회하면서
    for i in range(n):
        # 만약 visited list에 0이 남아있다면
        if 0 in visited:
            # 0이 남아있는 위치를 f_node로 설정해 준 이후
            f_node = visited.index(0)
            # f_node가 i와 같다면
            if f_node == i:
                # dfs를 통해 한 노드에 직접, 간접적으로 연결되어 있는 노드 탐색한다.
                dfs(f_node, graph, visited)
                # 탐색 이후 answer에 1을 더해준다.
                answer += 1
            # f_node가 i와 같지 않다면
            else:
                # 그냥 넘어간다.
                continue

    # answer를 반환한다.
    return answer
