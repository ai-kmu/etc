'''
BFS 사용
'''
from collections import deque


class Solution:
    def openLock(self, deadends, target):
        # deadends를 저장하기 위한 집합
        deadends = set(deadends)
        
        # BFS의 초기 상태 설정
        start = '0000'
        if start in deadends:
            return -1
        # BFS를 위한 deque 생성
        queue = deque([(start, 0)])
        # 방문 확인
        visited = set(start)
        
        # BFS 진행
        while queue:
            state, turns = queue.popleft()
            if state == target:
                return turns
            # 탐색
            for i in range(4):
                # 증가하는 방향으로 탐색
                new_state = state[:i] + str((int(state[i]) + 1) % 10) + state[i+1:]
                if new_state not in visited and new_state not in deadends:
                    queue.append((new_state, turns+1))
                    visited.add(new_state)
                # 감소하는 방향으로 탐색
                new_state = state[:i] + str((int(state[i]) - 1) % 10) + state[i+1:]
                if new_state not in visited and new_state not in deadends:
                    queue.append((new_state, turns+1))
                    visited.add(new_state)
                    
        # 불가능한 경우
        return -1
