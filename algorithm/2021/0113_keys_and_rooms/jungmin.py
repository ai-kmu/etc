class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [1] + [0 for _ in range(len(rooms) - 1)] # i번째 방 방문 여부 표시 리스트 생성
        visited_room = [0] # 방문한 방 기록하는 리스트 생성. 0번째 방 먼저 들어가므로 일단 0으로 저장
        
        while visited_room: 
            current = visited_room.pop() # 최근 방문한 방 인덱스 뽑아서 current에 저장
            
            for i in rooms[current]: #current 번째 방의 key를 불러온다.
                if visited[i] == 0: 
                    visited[i] = 1 # 처음 방문 한 방은 visited값을 1로 저장
                    visited_room.append(i) # 방문한 방을 기록하는 리스트 visited_room에 i 저장
                    
        return all(visited) # 최종적으로 visited 리스트에서 하나라도 0이 존재하면 False를 출력. 0이라는 것은 결국 그 방에 방문을 못했다는 의미이다.
