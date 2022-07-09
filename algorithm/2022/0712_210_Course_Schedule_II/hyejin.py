from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 들어야하는 course => numCourses
        # prerequisites = [a, b] => a를 듣기 위해서 b를 들어야함 a -> b
        # 들어야하는 순서대로 들을 수 있다면 순서 array
        # 만약 불가능하면 [] 반환
        # topological sort and dfs
        
        def dfs(graph, start):
            if self.visit[start]: # 들렀던 곳이면 패스
                return
            self.curr_path[start] = True
            self.visit[start] = True
            for post in graph[start]:
                if self.curr_path[post]: # 다음 가야할 곳이 이전에 있었는지 체크 / cycle이 있는지 확인
                    self.fail = True
                    return
                else:
                    dfs(graph, post)
            self.answer.append(start)
            self.curr_path[start] = False # path 끝남
        
        if len(prerequisites) == 0:
            return range(numCourses)
        
        # b -> a / b를 먼저 듣고 a로 가야함
        prerequisites_arr = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            prerequisites_arr[b].append(a)
        
        self.answer = [] # 정답
        self.visit = [False for _ in range(numCourses)] # 방문 체크
        self.curr_path = [False for _ in range(numCourses)] # 현재 돌고있는 path 체크
        self.fail = False # fail할 경우 => cycle이 있어, 실패하는 경우
        for node in range(numCourses):
            if self.visit[node] is False:
                dfs(prerequisites_arr, node)
            
            if self.fail:
                return []
            
        self.answer.reverse()
        return self.answer
                        
    
