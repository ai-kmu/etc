# 풀이 실패. 풀이 안 해주셔도 됩니다...

# [[0,0,1,1],[0,0,2,1],[1,0,2,1],[0,2,2,3]]
# Output: true
# Expected: false

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')
        total_area = 0
        corners = set()

        for x, y, a, b in rectangles:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, a)
            max_y = max(max_y, b)

            total_area += (a - x) * (b - y)

            all_points = [(x, y), (x, b), (a, y), (a, b)]
            for point in all_points:
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)

        big_square_area = (max_x - min_x) * (max_y - min_y)
        if total_area != big_square_area:
            return False

        if len(corners) != 4:
            return False

        return True
