from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        a = deque()
        # 이게 핵심이다
        # list로 방문처리했더니 시간에러가 발생함
        visited = set()
        a.append(start)
        if arr[start] == 0:
            return True
        # bfs
        while a:
            v = a.popleft()
            visited.add(v)
            if arr[v] == 0:
                return True
            if v+arr[v] < len(arr) and v+arr[v] not in visited:
                a.append(v+arr[v])
            if v-arr[v] > -1 and v-arr[v] not in visited:
                a.append(v-arr[v])
        return False
