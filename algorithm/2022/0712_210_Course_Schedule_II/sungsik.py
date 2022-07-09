class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 그래프를 adjacency list로 만듦
        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[b].append(a)
        
        answer = []
        visited = [False] * numCourses
        
        # dfs로 수행하면서 늦게 실행한 순서대로 node를 answer에 추가
        def dfs(node, tmp_visited):
            visited[node] = True
            tmp_visited[node] = True
            for neighbor in adj_list[node]:
                # cycle 체크
                if tmp_visited[neighbor]:
                    return True
                if not visited[neighbor]:
                    if dfs(neighbor, tmp_visited):
                        return True
            answer.append(node)
            tmp_visited[node] = False
            return False
        
        # 모든 node에 대해 순회하면서 dfs를 수행
        # 기존 search와 달리 늦게 수행한 순서대로 추가한 후 마지막에 뒤집음
        # 이유는 course의 번호순이 우선순위가 아니기 때문
        for i in range(numCourses):
            if not visited[i]:
                # dfs를 수행하면서 이미 visit한 node를 다시 가리킨다면 이는 cycle이 존재하는 것이다.
                tmp_visited = [False] * numCourses
                if dfs(i, tmp_visited):
                    return []
        
        return answer[::-1]
            
