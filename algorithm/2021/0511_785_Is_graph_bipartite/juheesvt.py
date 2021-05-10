class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
    
        current = 0
        
        color = [-1 for i in range(len(graph))]
        queue = []
        
        # 모든 정점 i에 대해서
        for i in range(len(graph)):
            
            # 해당 노드를 방문했으니까 색 바꿔주고 queue에 추가하기
            if color[i] == -1:
                color[i] = 1;
                queue.append(i)
            
            # queue가 빌때까지
            while len(queue) != 0:
                u = queue[0]
                del queue[0]
                
                # 현재 노드 u의 모든 이웃노드에 대하여
                for v in graph[u]:
                    
                    # XOR 연산으로 인접한 노드끼리 다른 색 만들어주기
                    if color[v] == -1:
                        color[v] = 1 ^ color[u]
                        # 다음 방문 노드에 v 추가 !
                        queue.append(v)
                    
                    elif color[v] == color[u]:
                        return False
                
        return True
                
        
        
        
# Union find
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def find(i):
            if roots[i] != i:
                roots[i] = find(roots[i])
            return roots[i]

        if not graph:
            return False
        roots = [i for i in range(len(graph))]
        for i in range(len(graph)):
            if graph[i]:
                ri = find(i)
                rj = find(graph[i][0])
                if ri == rj:
                    return False
                for k in range(1, len(graph[i])):
                    rk = find(graph[i][k])
                    if ri == rk:
                        return False
                    roots[graph[i][k]] = rj
        return True
"""
