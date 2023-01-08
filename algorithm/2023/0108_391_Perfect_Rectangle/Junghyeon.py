from collections import defaultdict


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        direct = defaultdict(lambda: [0, 0, 0, 0])        
        x = float('inf')
        a = float('-inf')
        y = float('inf')
        b = float('-inf')

        for rectangle in rectangles:
            x1, y1, a1, b1 = rectangle
            x = min(x, x1)
            a = max(a, a1)
            y = min(y, y1)
            b = max(b, b1)

        total_area = 0

        for rectangle in rectangles:
            x1, y1, a1, b1 = rectangle
            print(x1, y1, a1, b1)
            total_area += (a1 - x1) * (b1 - y1)
            direct[(x1, y1)][0] += 1
            direct[(x1, b1)][1] += 1
            direct[(a1, b1)][2] += 1
            direct[(a1, y1)][3] += 1
        
        # 사각형들의 합이 전체 사각형의 합과 다른경우 -> prefect rectangle x
        if total_area != (a-x) * (b-y):
            return False
        
        # 겹치는 사각형이 있는 경우에는 합이 같더라도 prefect rectangle를 만족하지 않는 경우 존재
        for key in direct:
            if key not in [(x, y), (x, b), (a, y), (a, b)]:
                if direct[key] not in [[1, 1, 1, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]]:
                    return False
        return True
