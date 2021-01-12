class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        check = [True]+[False]*(len(rooms)-1)
        
        keys = rooms[0]                     # 0번방 keys stack에 넣기
        
        while len(keys)>0:                  # stack이 텅 빌때까지 검사
            my_room = keys.pop()            # pop해서 그 방 방문 후 체크
            if check[my_room]==True: 
                continue
            check[my_room] = True
            
            for key in rooms[my_room]:      # 그 방에 있는 키 stack에 넣기
                if check[key]==True:
                    continue
                keys.append(key)
                   
        return False if False in check else True
