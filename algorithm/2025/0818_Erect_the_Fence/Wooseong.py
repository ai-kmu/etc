class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # 기울기 차 구하는 함수
        def tan_diff(a, b, c) -> int:
            '''
            ab와 bc 사이의 기울기 차는
            (cy - by)   (by - ay)   (cy - by)(bx - ax) - (by - ay)(cx - bx)
            --------- - --------- = ---------------------------------------
            (cx - bx)   (bx - ax)             (cx - bx)(bx - ax)          
            여기서 이미 sorting 해둬서 분모는 항상 0 이상이므로
            기울기 차의 부호는 분자만 가지고 판별 가능
            '''
            return (c[1] - b[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - b[0])

        # 정렬 - tuple로 해두면 정답 형식 맞추기 편함
        points = sorted(map(tuple, trees))

        lower = []
        upper = []
        for point in points:
            while len(lower) >= 2 and tan_diff(lower[-2], lower[-1], point) > 0:
                # 새로운 point로 인해 기울기가 커지면 볼록성이 깨짐
                lower.pop()
            while len(upper) >= 2 and tan_diff(upper[-2], upper[-1], point) < 0:
                # 새로운 point로 인해 기울기가 작아지면 볼록성이 깨짐
                upper.pop()
            lower.append(point)
            upper.append(point)

        hull = set(lower + upper)
        return [list(p) for p in hull]

