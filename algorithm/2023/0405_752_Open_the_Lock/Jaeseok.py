import copy
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        q = deque()
        # 현재 위치와 움직인 횟수를 저장함
        q.append((['0', '0', '0', '0'], 1))
        # 0000이 target인 경우
        if target == '0000':
            return 0
        # 0000에서 벗어날 수 없는 경우
        if '0000' in deadends:
            return -1
        # BFS
        while q:
            wheel, answer = q.popleft()
            # 각 자릿수 순회
            for i in range(4):
                # 앞으로 돌리는 경우와 뒤로 돌리는 경우
                for j in (-1, 1):
                    tmp = str(int(wheel[i]) + 1*j)
                    if tmp == '10':
                        tmp = '0'
                    elif tmp == '-1':
                        tmp = '9'
                    new_wheel = copy.deepcopy(wheel)
                    new_wheel[i] = tmp
                    num = ''.join(new_wheel)
                    # num이 타겟과 같을 경우 움직인 거리 return
                    if num == target:
                        return answer
                    # 새로 이동한 곳이 아직 방문하지 않았고 deadend가 아닐 경우 큐에 추가
                    if num not in visited and num not in deadends:
                        visited.add(num)
                        q.append((new_wheel, answer+1))
        # 전부 순회했을 때도 발견하지 못했으면 -1 return
        return -1
