class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [] #방문한 방의 리스트
        keys = deque() #현재 방에 있는 열쇠

        keys.append([0]) #첫번째 방에 들어가기 위해 0번째 방의 열쇠를 추가한다.
        
        while keys:
            key = keys.popleft() #다음 방을 열기 위한 열쇠
      
            for i in key:
                if i not in visited: #다음 방의 열쇠는 있지만 방문한 방이 아닐경우
                    keys.append(rooms[i]) #keys에 현재 방에 있는 열쇠들을 추가한다.
                    visited.append(i) # 현재 방문한 방을 표시
    
        if len(visited)==len(rooms): #만약 방문의 방의 개수와 전체 방의 개수가 같다면 True리턴
            return True
        
        else: return False
