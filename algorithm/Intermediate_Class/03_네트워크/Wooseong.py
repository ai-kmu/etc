def solution(n, computers):
    answer = 0
    visited = set()

    # DFS
    def DFS(start):
        # 모든 computer 탐색
        for i in range(n):
            # 자기 자신 건너 뛰고
            if i == start:
                continue
            # 자기와 연결된 애들 중 방문 안 한 애 있으면 넣고 DFS
            if computers[start][i] and (i not in visited):
                visited.add(i)
                DFS(i)

    # 모든 노드에 대해서
    for start in range(n):
        # 방문하지 않았으면 넣고 DFS
        if start not in visited:
            visited.add(start)
            DFS(start)
            answer += 1

    return answer
