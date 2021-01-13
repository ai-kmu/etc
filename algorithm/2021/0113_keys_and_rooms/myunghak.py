# 탐색 문제
# dfs로 탐색 가능한지만 판단

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(current):
            blank[current] = False #현재거 방문했다고 체크
            [dfs(i) for i in filter(lambda x: blank[x], rooms[current])] # 현재 노드와 연결된것 중 방문한거 빼고 dfs 돌리기
            
        
        blank = [True for i in range(len(rooms))]
        dfs(0)      
        
        return sum(blank) == 0
