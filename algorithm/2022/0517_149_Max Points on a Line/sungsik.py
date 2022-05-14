from fractions import Fraction

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 1
        
        lines = dict()
        
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i+1:]:
                # x1, x2가 같으면 직선을 단순히 x절편으로 표시
                if x1 == x2:
                    lines[x1] = lines.get(x1, 0) + 1
                else:
                    # m: 기울기, n: y절편
                    # m을 단순히 (y2-y1)/(x2-x1)으로 하면 소수가 무한할때 key값으로 활용할 수 없음
                    # 따라서 Fraction 라이브러리 활용
                    m = Fraction(y2-y1, x2-x1)
                    n = y1 - m * x1
                    lines[(m, n)] = lines.get((m, n), 0) + 1
        
        # 근의 공식을 써서 Combination(n, 2)를 n으로 치환
        # n(n-1)/2 = k
        # n^2 - n + 2K = 0
        # n = (1 + root(1 + 8k)) / 2
        return (1 + int((1 + 8 * max(lines.values())) ** 0.5)) // 2
