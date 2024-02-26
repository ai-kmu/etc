# DFS? BFS?
# start에서 depth를 1만큼 계속 증가시켜서 BFS로 탐색
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        visited = [False] * len(arr)
        visited[start] = True

        deq = deque([start])

        while len(deq):
            idx = deq.popleft()
            
            if not arr[idx]:
                return True
            
            # 다음으로 탐색할 왼쪽, 오른쪽에 대한 인덱스 정보
            right = idx + arr[idx]
            left = idx - arr[idx]
                
            if -1 < right < len(arr):
                if visited[right] == False:
                    visited[right] = True
                    deq.append(right)
                
            if -1 < left < len(arr):
                if visited[left] == False:
                    visited[left] = True
                    deq.append(left)

        return False
