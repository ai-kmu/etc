from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        # 방문한 node와 방향을 visited에 담는다.
        visited = {(0, False)}
        
        # queue에는 node위치, 순회한 횟수, 방향을 담는다.
        q = deque()
        q.append((0, 0, False))
        
        # bfs로 node를 찾아나간다.
        while q:
            pos, turns, backward = q.popleft()
            
            # 해당 node가 원하는 node일 경우 turn을 return한다.
            if pos == x:
                return turns
            
            # a만큼 앞으로 나아간 후
            nextPos = pos + a
            # 범위 이내이고, forbidden에 없고, visit한적이 없으면 queue에 추가한다.
            if 0 <= nextPos <= 6000 and not nextPos in forbidden and not (nextPos, False) in visited:
                q.append((nextPos, turns+1, False))
                visited.add((nextPos, False))
            
            # b만큼 뒤로 나아간 후
            nextPos = pos - b
            # 범위 이내이고, forbidden에 없고, visit한 적이 없으며, 이전 방향이 backward가 아니면 queue에 추가한다.
            if 0 <= nextPos <= 6000 and not nextPos in forbidden and not (nextPos, True) in visited and not backward:
                q.append((nextPos, turns+1, True))
                visited.add((nextPos, True))
        
        return -1
