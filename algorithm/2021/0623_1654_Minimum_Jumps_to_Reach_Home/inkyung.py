from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        visited = set()
        que = deque([[0, 0, False]])
        
        # 최대로 갈 수 있는 경우 - x나 forbidden중 가장 큰값 + a + b
        limit = max(x, max(forbidden)) + a + b

        while que:
            pos, cnt, back = que.popleft()
            # print(pos, cnt, back)
            if pos > limit or pos < 0 or pos in forbidden or (pos, back) in visited:
                continue
            if pos == x:
                return cnt
            # 앞으로 움직일 때 계산 + 뒤로 간게 아니기 때문에 False 포함
            que.append([pos + a, cnt + 1, False])
            
            if not back:        # 뒤로 간게 아니면 앞이랑 뒤 모두 체크
                que.append([pos - b, cnt + 1, True])
            visited.add((pos, back))
            # print(que)
        return -1
