from collections import deque
class Solution:
    def canReach(self, arr, start):
        def bfs(self, arr, start):
            N = len(arr)
            queue = deque([start])
            visited = {start}
            
            # 앞뒤로 하나씩 보면서 방문처리
            while queue:
                i = queue.popleft()
                if i<0 or i>=N:
                    continue
                if arr[i] == 0:
                    return True
                
                if i+arr[i] not in visited:
                    visited.add(i+arr[i])
                    queue.append(i+arr[i])
                
                if i-arr[i] not in visited:
                    visited.add(i-arr[i])
                    queue.append(i-arr[i])
            
            return False


        return bfs(self, arr, start)

    

