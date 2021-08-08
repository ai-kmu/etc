from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visits = [False for _ in range(len(rooms))]
        visits[0] = True
        queue = deque(rooms[0])
        # queue를 이용하여 들린 방에서 키들을 queue에 넣음
        # 하나씩 빼면서 visit 표시 해줌. queue가 빌 때까지 수행
        while queue:
            curr = queue.popleft()
            visits[curr] = True
            for i in rooms[curr]:
                if visits[i] is False:
                    queue.append(i)
            
        return False if False in visits else True
            
