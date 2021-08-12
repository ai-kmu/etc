class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:  
        visited = [0 for _ in range(len(rooms))] # 방문했던 곳 기록을 위한 리스트
        visited[0] = 1 # 처음 인덱스 0 방은 방문가능하므로 방문했다고 기록
        v_room = [0] # 방문 가능하거나 방문한 인덱스 방 기록
        
        while v_room:
            # v_room의 요소가 없을 때까지 방문 가능한 방 하나씩 뽑아서 방문했던 적이 없으면 visited 리스트에서 해당 인덱스의 값을 1로 바꾼다.
            now_visit = v_room.pop() 
            for i in rooms[now_visit]: 
                if not visited[i]: 
                    visited[i] = 1 
                    v_room.append(i)
                    
        for i in visited:
            if i == 0: return False # 하나라도 방문한 적이 없는 방이 있으면 False 반환
                    
        return True # 모두 방문한 적이 있으면 True 반환
