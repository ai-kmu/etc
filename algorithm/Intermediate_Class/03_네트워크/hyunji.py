def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for v in range(n):
        # 방문하지 않았을 때만 dfs로 탐색
        if visited[v] == False:
            dfs(n, computers, visited, v)
            answer += 1
    return answer

def dfs(n, computers, visited, v):
    # 방문처리
    visited[v] = True
    for i in range(n):
        # 연결 되어있고 아직 방문하지 않은 컴퓨터인 경우 dfs 탐색
        if computers[v][i] == 1 and visited[i] == False:
            dfs(n, computers, visited, i)
