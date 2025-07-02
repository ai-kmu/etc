from collections import defaultdict


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 효율성을 위해 tuple의 set으로 변환
        obstacles = set([(x, y) for x, y in obstacles])
        # 북 서 남 동
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        dir_idx = 0
        x, y = 0, 0

        rotate = lambda idx, turn: (idx + turn) % 4

        answer = 0
        for command in commands:
            # 회전
            if command == -1:
                dir_idx = rotate(dir_idx, -1)
            elif command == -2:
                dir_idx = rotate(dir_idx, 1)
            # 직진
            else:
                dx, dy = dirs[dir_idx]
                for _ in range(command):
                    x += dx
                    y += dy
                    # 막힐 경우 stop
                    if (x, y) in obstacles:
                        x -= dx
                        y -= dy
                        break
                    answer = max(answer, x ** 2 + y ** 2)
        return answer
        
