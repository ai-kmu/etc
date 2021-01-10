class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]                                                   # 방문한 방을 저장하는 리스트
        w_visit = deque(list(set(rooms[0])))                            # 방문 가능한 방을 저장하는 deque
        while w_visit:                                                  # 방문 가능한 방을 모두 갈때까지
            now = w_visit.popleft()                                     # 방문 가능한 방에서 하나를 뽑아
            visited.append(now)                                         # 방문한 리스트에 넣고
            for room_num in list(set(rooms[now])):                      # 그 방에 있는 열쇠들 중
                if room_num not in visited and room_num not in w_visit: # 방문한 곳 또는 방문 가능한 곳이 아닌 경우
                    w_visit.append(room_num)                            # deque에 저장
        if len(visited) == len(rooms):                                  # 모든 방을 돈 경우
            return True                                                 # True 반환
        return False                                                    # 아닌 경우 False 반환
