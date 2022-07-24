# 1. DFS로 가능한 경로를 모두 탐색하여 answer 배열에 넣어주고,
# 2. answer 배열을 정렬해서 가장 처음 경로를 return 해줌

import copy
def solution(tickets):
    
    visited = [0 for _ in range(len(tickets))]
    answer = []
    result = ["ICN"]
    
    def dfs(start, visited, result):
        
        # 도시를 모두 방문하는 경로인 경우 (탐색이 끝난 경우)
        if len(result) == len(tickets) + 1:
            # 정답 배열에 현재 경로를 넣어줌
            answer.append(result)
            return
        
        for i in range(len(tickets)):
            # 현재 도시가 출발지이면서 아직 방문하지 않은 도착지인 경우,
            if tickets[i][0] == start and visited[i] == 0:
                tmp_result = copy.deepcopy(result)
                # 방문 처리
                visited[i] = 1 
                # 현재 경로에 도착지를 추가
                tmp_result.append(tickets[i][1])
                # dfs 탐색
                dfs(tickets[i][1], visited, tmp_result)
                visited[i] = 0
    
    dfs("ICN", visited, result)
    answer = sorted(answer)
    
    return answer[0]
    
