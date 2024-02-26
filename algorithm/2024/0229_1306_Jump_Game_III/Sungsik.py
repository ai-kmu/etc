from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # BFS
        n = len(arr)
        visited = [False] * n
        
        queue = deque([start])
        visited[start] = True
        
        # 더이상 visit할게 없을때까지 순회
        while queue:
            idx = queue.popleft()
            if arr[idx] == 0:
                return True
            
            left, right = idx - arr[idx], idx + arr[idx]

            if left >= 0 and not visited[left]:
                visited[left] = True
                queue.append(left)
            
            if right < n and not visited[right]:
                visited[right] = True
                queue.append(right)
        
        return False
