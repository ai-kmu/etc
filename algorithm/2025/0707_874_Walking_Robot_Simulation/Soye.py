class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 동, 남, 서, 북 순서로 방향 정의
        obstacle_set = {tuple(obs) for obs in obstacles}  # 장애물을 집합으로 변환 (빠른 탐색을 위해)

        idx, x, y, res = 3, 0, 0, 0  # idx: 현재 방향(초기 북쪽), (x, y): 현재 위치, res: 최대 거리 제곱값

        for e in commands:
            if e == -2:
                idx = (3 + idx) % 4  # 왼쪽으로 90도 회전
            elif e == -1:
                idx = (1 + idx) % 4  # 오른쪽으로 90도 회전
            else:
                dx, dy = dirs[idx]  # 현재 방향의 단위 벡터
                for _ in range(e):  # 한 칸씩 이동
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacle_set:  # 장애물 만나면 멈춤
                        break
                    x, y = nx, ny  # 위치 업데이트
                    res = max(res, x * x + y * y)  # 최대 거리 제곱값 업데이트

        return res  # 최대 거리 제곱값 반환
