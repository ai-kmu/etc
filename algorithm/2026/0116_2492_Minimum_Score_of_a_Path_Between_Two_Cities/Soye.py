# 솔루션 참고했습니다.
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj=[]
        related=set()
        for i in range(n+1):
            adj.append([])
        for i in roads:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        def dfs(node:int):
            related.add(node)
            for i in adj[node]:
                if i not in related:
                    dfs(i)
        dfs(1)
        dfs(n)
        res=10000
        for i in roads:
            if i[0] in related and i[1] in related:
                res=min(res,i[2])
        return res
