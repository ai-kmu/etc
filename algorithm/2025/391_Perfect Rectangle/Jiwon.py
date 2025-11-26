class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x = min_y = float('inf')
        max_a = max_b = float('-inf')

        check = 0  # 모든 네모 합
        ans = set()

        for x, y, a, b in rectangles:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            check += (a - x) * (b - y)

            # 꼭짓점 XOR
            for point in ((x, y), (x, b), (a, y), (a, b)):
                if point in ans:
                    ans.remove(point)
                else:
                    ans.add(point)

        # 겹치거나 빈틈 존재
        if check != (max_a - min_x) * (max_b - min_y):
            return False

        gt = {(min_x, min_y), (min_x, max_b), (max_a, min_y), (max_a, max_b)}
        return ans == gt
