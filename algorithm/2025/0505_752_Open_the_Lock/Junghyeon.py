# BFS
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)

        # 시작점이 막혀있으면 바로 종료
        if "0000" in dead_set:
            return -1

        visited = set()
        visited.add("0000")

        queue = deque()
        queue.append(("0000", 0))

        while queue:
            current, steps = queue.popleft()

            if current == target:
                return steps

            # 4자리의 각 숫자를 위, 아래로 돌려봄
            for i in range(4):
                num = int(current[i])
                up = (num + 1) % 10
                down = (num - 1 + 10) % 10

                for move in [up, down]:
                    new_combo = current[:i] + str(move) + current[i+1:]

                    if new_combo not in dead_set and new_combo not in visited:
                        visited.add(new_combo)
                        queue.append((new_combo, steps + 1))

        return -1
