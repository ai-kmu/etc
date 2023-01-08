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

