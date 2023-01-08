# 작은 사각형과 큰 사각형의 넓이 차이로 문제를 해결해보려고 하였음
# 33/49 : 넓이 차이가 동일한 경우에는 안됨
# 수정중

cclass Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        gx_min, gx_max, gy_min, gy_max = 10**5, -10**5, 10**5, -10**5
        res_area = 0
        for x_min, y_min, x_max, y_max in rectangles:
            gx_min = min(x_min, gx_min)
            gy_min = min(y_min, gy_min)
            gx_max = max(x_max, gx_max)
            gy_max = max(y_max, gy_max)
            res_area += (x_max - x_min) * (y_max - y_min)
        rect_area = (gx_max - gx_min) * (gy_max - gy_min)
        print(gx_min, gx_max, gy_min, gy_max)
        if res_area == rect_area:
            return True
        return False

# 수정한 코드

from collections import defaultdict


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # defaultdict로 꼭짓점을 세어줌
        vertex = defaultdict(int)
        # 전체 직사각형을 위한 좌표값
        gx_min, gx_max, gy_min, gy_max = 10**5, -10**5, 10**5, -10**5
        # 개별 넓이
        res_area = 0
        for x_min, y_min, x_max, y_max in rectangles:
            # 각 꼭짓점을 defaultdict에 추가해줌
            vertex[(x_min, y_min)] += 1
            vertex[(x_min, y_max)] += 1
            vertex[(x_max, y_min)] += 1
            vertex[(x_max, y_max)] += 1

            # 전체 직사각형의 넓이를 구하기 위한 꼭짓점 갱신
            gx_min = min(x_min, gx_min)
            gy_min = min(y_min, gy_min)
            gx_max = max(x_max, gx_max)
            gy_max = max(y_max, gy_max)

            # 개별 직사각형의 넓이를 계산
            res_area += (x_max - x_min) * (y_max - y_min)

        # 전체 직사각형 넓이 계산
        rect_area = (gx_max - gx_min) * (gy_max - gy_min)

        # 전체 직사각형의 꼭짓점은 단 한개만 존재해야 함
        vertex[(gx_min, gy_min)] -= 1
        vertex[(gx_min, gy_max)] -= 1
        vertex[(gx_max, gy_min)] -= 1
        vertex[(gx_max, gy_max)] -= 1

        # 개별 사각형 넓이가 전체 사각형 넓이와 다르면 겹치는 넓이가 존재한다는 것을 의미
        if res_area != rect_area:
            return False

        # 나머지 꼭짓점들은 짝수로 겹쳐야 함
        for v in vertex.values():
            if v % 2 != 0:
                return False

        return True
