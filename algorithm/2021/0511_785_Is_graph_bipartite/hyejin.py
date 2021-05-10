class Solution:
    def dfs(self, u, graph, visit, color):
        stack = deque([[u, color]]) 
        while stack:
            node, color = stack.pop()
            visit[node] = [True, color] # visit update
            for v in graph[node]:
                if visit[v][1] == color: # u color와 v의 color가 같을 때는 이분그래프가 되지 않음.
                    return False
                
                if visit[v][0] is False:
                    # 기존 color와 반대로 color를 할당
                    stack.append([v, 1-color])
                    
        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visit = [[False, -1] for i in graph] # 방문했는지, 어떤 set에 속하는지
        
        for i in range(len(graph)): # 방문하지 않은 node들을 방문
            if visit[i][0] is False:
                if not self.dfs(i, graph, visit, 0): # dfs 수행
                    return False
                
        return True
