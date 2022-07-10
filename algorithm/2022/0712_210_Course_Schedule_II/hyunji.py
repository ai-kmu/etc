# graph 생성 후 dfs 사용해서 graph 탐색
# dfs 를 통해서 cycle이 생기는지 확인
#    1. cycle이 생기는 경우(visitied[i] = False) [] 를 return
#    2. cycle이 생기지 않는 경우(visitied[i] = True) 현재 node를 append

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        answer = []
        
        # cycle이 생기지 않아서 수강하면 visited[i] = True
        visited = [None] * numCourses
        graph = [[] for _ in range(numCourses)]
        
        # 그래프 생성
        for now, prerequisite in prerequisites:
            graph[now].append(prerequisite)
            
            
        def dfs(now):
            if visited[now]:
                return True
            
            if visited[now] == False:
                return False
            
            visited[now] = False

            # dfs로 탐색하며 cycle이 생기는지 확인
            for prerequisite in graph[now]:
                if not dfs(prerequisite):
                    return False
                
            answer.append(now)
            visited[now] = True
            
            return True
        
        
        for vertex in range(numCourses):
            if not dfs(vertex):
                return []

        return answer
