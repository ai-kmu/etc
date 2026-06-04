# 솔루션
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)
        connected=[ [] for i in range(n)]

        for i in range(n):
            sm=[]
            for j in range(n):
                if j!=i:
                    xi, yi, ri = bombs[i]
                    xj, yj, _ = bombs[j]
                    if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                        sm.append(j)
            connected[i]=sm
        res=[]
        visited=[]
      
        def dfs(i:int):
            if i not in visited:
                visited.append(i)
                for j in connected[i]:
                    dfs(j)
                
        for i in range(n):
            visited.append(i)
            for j in connected[i]:
                dfs(j)
            res.append(len(visited))
            visited.clear()

        return max(res)
        
 
