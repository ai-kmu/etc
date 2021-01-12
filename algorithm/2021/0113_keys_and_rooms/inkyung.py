class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 0번째 방은 그냥 들어갈 수 있기 때문
        visited = set([0])
        
        def dfs(keys):
            for key in keys:
                # 아직 안간 방이면
                if key not in visited:
                    # 들어가고
                    visited.add(key)
                    # 그 방의 키를 가지고 다시 서칭
                    dfs(rooms[key])            
        
        dfs(rooms[0])
    
        return len(visited) == len(rooms)
            
