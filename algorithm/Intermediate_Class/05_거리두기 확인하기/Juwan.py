class Room:
    
    def __init__(self, room):
        self.room = room
        self.valid = True

def solution(places):
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    rooms = []
    
    for i in range(5):
        for j in range(5):
            places[i][j] = list(places[i][j])
        rooms.append(Room(places[i]))
        
    def dfs(cls_room, i, j, depth):
        
        if depth == 3:
            return
        
        if cls_room.room[i][j] == 'V':
            return
        
        if cls_room.room[i][j] == 'X':
            return
        
        if cls_room.room[i][j] == 'P' and depth != 0:
            cls_room.valid = False
            return
        
        if cls_room.valid == False:
            return
        
        cls_room.room[i][j] = 'V'
        depth += 1
        
        for x, y in zip(dx, dy):
            
            if (0 <= i - x < 5) and (0 <= j - y < 5):
                
                dfs(cls_room, i-x, j-y, depth)
        
            
    for r in rooms:
        
        for i in range(5):
            
            for j in range(5):
                
                if r.room[i][j] == 'P':
                    
                    dfs(r, i, j, 0)
                
                    if r.valid == False:
                        break
    
    answer = []
    for i in rooms:
        ans = 1 if i.valid == True else 0
        answer.append(ans)
        
    
    return answer
