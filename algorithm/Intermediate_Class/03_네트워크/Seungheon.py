def solution(n, computers):
    answer = 0
    visited = n*[0]

    def explore(node):
        nonlocal answer
        nonlocal basenode
        
        #  방문한 node 무시
        if visited[node] == 1:
            return 

        # 현재 node 방문처리
        visited[node] = 1
        
        # 현재 node에서 갈 수 있는 node로 이동
        for next_node, link in enumerate(computers[node]):
            if link == 1:
                explore(next_node)

				# 방문하지 않은 basenode에 한에서 탐색시 answer을 추가
        if basenode == node:
            answer+=1
            
    # 모든 노드에 대해서 실행
    for node in range(n):
        basenode = node
        explore(node)
        
    return answer
