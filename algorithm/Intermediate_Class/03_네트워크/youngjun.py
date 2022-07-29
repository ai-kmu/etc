# Sol 1) BFS

from collections import deque

def solution(n, computers):
    answer = 0
    graph = {node:[] for node in range(n)}
    visited = [0]*n

    def bfs(n):
        queue = deque()
        queue.append(n)
        while queue:
            node = queue.popleft()
            if visited[node] == 0:
                visited[node] = 1
                for i in graph[node]:
                    queue.append(i)
        return visited    
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)

    for i in range(n):
        if 0 in visited:
            f_node = visited.index(0)
            if f_node == i:
                bfs(f_node)
                answer += 1
            else:
                continue

    return answer
