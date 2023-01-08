import bisect

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 문제 조건을 충족시키려면
        # 큰 정사각형의 꼭짓점을 제외한 모든 꼭짓점이 2번 아니면 4번 등장해야 한다
        points = set()
        total_area = 0
        for x1, y1, x2, y2 in rectangles:
            total_area += (x2 - x1) * (y2 - y1)
            # 모든 꼭짓점을 XOR 연산을 거쳐 홀수번 등장하면 남기고, 짝수번 등장하면 없앤다.
            points ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}

        # 4개의 꼭짓점만 남아있어야 함
        if len(points) != 4:
            return False
        
        # area도 체크
        xs = [p[0] for p in points]
        xl, xr = min(xs), max(xs)
        ys = [p[1] for p in points]
        yl, yr = min(ys), max(ys)
        return total_area == (xr - xl) * (yr - yl)
