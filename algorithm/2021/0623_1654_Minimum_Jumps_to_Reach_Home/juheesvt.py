
"""
BFS (너비 우선 탐색) 를 활용하여 해결할 수 있음

먼저 최대로 갈 수 있는 위치인 max_val을 초기화
lookup이라는 방문 체크 리스트를 만드는데, forbidden에 포함된 위치는 갈 수 없으므로, lookup에 모두 기록함
그리고 0부터 차례대로 큐에 넣어서 탐색 시작 !

아래와 같은 case로 나눠서 탐색
현재위치(pos) == home(x)
 - 현재위치에서 앞(a)으로 갈 수 있으면서, 해당 위치를 방문 X
이미 방문했을 때
 - 현재위치에서 뒤(b)으로 갈 수 있으면서, 해당 위치를 방문 X
 - 첫번째 케이스에서 리턴이 안되고 while문을 빠져나오면 -1 리턴
"""

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        max_f = max(forbidden)


        max_val = x + b if a >= b else max(x, max_f) + a + (b + a)
        lookup = set()
        for pos in forbidden:
            lookup.add((pos, True))
            lookup.add((pos, False))
        result = 0
        q = [(0, True)]
        lookup.add((0, True))
        while q:
            new_q = []
            for pos, can_back in q:
                if pos == x:
                    return result
                if pos + a <= max_val and (pos + a, True) not in lookup:
                    lookup.add((pos + a, True))
                    new_q.append((pos + a, True))
                if not can_back:
                    continue
                if pos - b >= 0 and (pos - b, False) not in lookup:
                    lookup.add((pos - b, False))
                    new_q.append((pos - b, False))
            q = new_q
            result += 1
        return -1
