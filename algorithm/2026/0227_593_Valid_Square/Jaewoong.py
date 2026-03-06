from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]

        def dist2(a: List[int], b: List[int]) -> int:
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            return dx*dx + dy*dy

        dists = []
        for i in range(4):
            for j in range(i + 1, 4):
                dists.append(dist2(points[i], points[j]))

        dists.sort()

        # 변 길이 0이면(점이 겹치면) 정사각형 불가
        if dists[0] == 0:
            return False

        side = dists[0]
        diag = dists[-1]

        # 4개의 변: 같은 길이 4개
        if not (dists[0] == dists[1] == dists[2] == dists[3] == side):
            return False

        # 2개의 대각선: 같은 길이 2개
        if not (dists[4] == dists[5] == diag):
            return False

        # 정사각형 성질: 대각선^2 = 변^2 * 2
        return diag == 2 * side
