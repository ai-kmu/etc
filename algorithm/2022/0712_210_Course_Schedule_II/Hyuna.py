# 실패
from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        
        g = Graph(numCourses)
        
        # add edges
        for pre in prerequisites:
            g.addEdge(pre[0], pre[1])
        
        return g.topologicalSort()
        
        

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def topologicalSortRe(self, v, visited, stack):
        visited[v] = True
        
        # 연결된 꼭지점 방문을 위한 for문 
        for i in self.graph[v]:
            if v in self.graph[i]: # 서로가 서로의 prerequisite일때 
                stack = [];
                return stack;
            if visited[i] == False:
                self.topologicalSortRe(i, visited, stack)
                
        stack.append(v)
        
    # 재귀 될 떄는 topologicalSortRe 사용 
    def topologicalSort(self):
        visited = [False] *self.V
        stack = []
        
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortRe(i, visited, stack)
            if len(stack) == 0:
                break;
                
        return stack
