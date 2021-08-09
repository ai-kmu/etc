
def canVisitAllRooms(rooms):
    queue = [] # 가지고있는 열쇠
    mem_queue = {0} #먹은 열쇠를 기억

    while queue:
        cur_num = queue.pop(0)
        cur_room = rooms[cur_num] 
        key = set(cur_room) - mem_queue # 방안에 열쇠중 먹은 열쇠를 제외한것 획득
        mem_queue = mem_queue | key 
        queue += list(key)
    if len(mem_queue) != len(rooms): #만약 획득한 열쇠와 방의 개수가 다르다면 False
        return False
    return True
