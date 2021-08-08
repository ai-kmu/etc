class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [0] + rooms[0]             # 0번째 방 키를 저장
        n_r = len(rooms)                  # 전체 방의 수 확인
        try:
            for i in range(1, n_r):       # 키를 가지고 방들을 방문하면서 
                for j in rooms[keys[i]]:  # 마지막까지 갖게된 키의 수가 전체 방 수보다 작으면 
                    if j not in keys:     
                        keys.append(j)
        except:                           
            return False
        return True
