class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(r, rooms):  #전형적 dfs 알고리즘 문제
            visited[r] = 1
            for n in rooms[r]:
                if not visited[n]:
                    dfs(n, rooms)
                    
        visited = [0]*len(rooms)
        dfs(0, rooms)
        
        return not 0 in visited
