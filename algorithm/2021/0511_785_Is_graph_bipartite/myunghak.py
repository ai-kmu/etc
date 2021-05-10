# dfs로 check를 해나가면서 진행하다 만약 색을 칠하는걸 실패하면 False로 return한다

class Solution:
    def __init__(self):
        self.check = []
    def dfs(self,graph, i, num): # graph의 i번째 노드는 num으로 check
        if self.check[i] == num:
            return True
        elif self.check[i] == -1:
            self.check[i] = num
            for node in graph[i]:
                if not self.dfs(graph, node, (num+1)%2):
                    return False
            return True
        else:
            return False
    
    def isBipartite(self, graph) -> bool:
        self.check = [-1] * len(graph)
        ans = True
        for i in range(len(graph)):
            ans = (ans and self.dfs(graph,i,0 if self.check[i] == -1 else self.check[i]))
        return ans
