class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 방문한 방을 저장하는 리스트
        visited = [False for _ in range(len(rooms))]
        # 0번 방은 True로 설정
        visited[0] = True
        # 열쇠를 저장하는 keys는 0번 방 안에 있는 key들로 초기화한다
        keys = deque(rooms[0])
        # 방문한 횟수는 1로 초기화
        visitNum = 1
        
        # keys가 비어있지 않을 때 까지 반복한다
        while keys:
            # 이미 방문한 방의 key들을 제거한다
            while visited[keys[0]]:
                keys.popleft()
                # key가 남아있지 않을 경우 False return
                if len(keys) == 0:
                    return False
            # 방을 방문한 후 방안에 있는 key들을 keys에 추가한다.
            key = keys.popleft()
            visited[key] = True
            keys += rooms[key]
            visitNum += 1
            # 방문 횟수가 총 방의 개수와 동일할 경우 True return
            if visitNum == len(rooms):
                return True
        return False
