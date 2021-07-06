class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        # 큐에 존재하는 모든 노드의 구성은 (위치, 마지막으로 뒤로 점프했는가, 현재까지의 step)
        q = collections.deque([(0, False, 0)])
        visited = set([0, False])
        upper_bound = 6000
        
        while q:
            for _ in range(len(q)):
                pos, back, steps = q.pop()
                if pos == x:
                    return steps # 위치에 도착하면 현재까지의 step 반환
                if 0 <= pos + a <= upper_bound and (pos + a, False) not in visited and pos + a not in forbidden:
                    visited.add((pos+a, back))
                    q.appendleft((pos+a, False, steps+1)) # 앞으로 한 칸 이동한 것을 추가하며 뒤로 가지 않았다는 것까지 정보 저장
                if not back and 0 <= pos-b <= upper_bound and (pos-b, True) not in visited and pos-b not in forbidden: 
                    visited.add((pos-b, True))
                    q.appendleft((pos-b, True, steps+1))  # 뒤로 한 칸 이동한 것을 추가하며 이후 차례에서 뒤로 이동하지 못하는 상황을 저장.
        return -1                   
