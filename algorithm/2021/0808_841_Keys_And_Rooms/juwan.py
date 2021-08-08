class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in range(len(rooms))]
        # 방의 개수만큼의 리스트를 만들어서 방문했다는 표시를 할 것임.
        
        def dfs(idx, visited):
            visited[idx] = True
            # 해당 idx번째 방을 방문함.
            # 해당 idx번째 방에 있는 열쇠들로 다른 방들을 탐색 시작 ( 재귀적으로 탐색 )
            for sub in rooms[idx]:
                if visited[sub]:
                    continue # 키를 갖고 찾는 방을 이미 방문했다면 계속함.
                elif not visited[sub]: # 새로운 방을 찾았다면 재귀 dfs
                    dfs(sub, visited)
                    
        
        dfs(0, visited)
        # 0번 방부터 시작하여 dfs 시작.
        
        if False in visited:
            return False
        else:
            return True
