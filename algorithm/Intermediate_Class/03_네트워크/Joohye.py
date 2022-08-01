def solution(n, computers):
    answer = 0
    visited = n*[0]
    stack = []
    
    # stack에 node추가 stack이 비면 answer 에 + 1
    # 방문한 노드이면 넘어가기
    
    def explore(node):
        nonlocal answer
        if visited[node] == 1:  # 방문한 node 무시
            return 
        # 현재 node stack에 추가
        stack.append(node)
        # 현재 node 방문처리
        visited[node] = 1
        # 현재 node에서 갈 수 있는 node로 이동
        for next_node, link in enumerate(computers[node]):
            if link == 1:
                explore(next_node)
        # 모든 node를 방문했으면 stack에서 pop
        stack.pop()
        # stack이 비면 answer에 + 1
        if not stack:
            answer += 1
    # 모든 노드에 대해서 실행
    for node in range(n):
        explore(node)
        
    return answer
