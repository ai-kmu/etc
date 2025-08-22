# 솔루션 참고 :: Monotone Chain algorithm

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # 세 점의 방향 판별
        # output > 0: 반시계
        # output < 0: 시계
        # output = 0 : 일직선 상에 위치
        def cross_product(p0, p1, p2):
            return (p1[0] - p0[0]) * (p2[1] - p0[1]) - \
                   (p1[1] - p0[1]) * (p2[0] - p0[0])

        # 점 정렬
        sorted_trees = sorted(trees)
      
        hull = []

        # Lower Hull (왼 -> 오)
        for p in sorted_trees:
            # 볼록성 깨는 경우 마지막 점 제거
            while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) < 0:
                hull.pop()
            hull.append(p)

        # Upper Hull (오 -> 왼)
        for p in reversed(sorted_trees):
            # 볼록성 깨는 경우 마지막 점 제거
            while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) < 0:
                hull.pop()
            hull.append(p)

        # set: 중복 제거 -> 이를 위해 tuple로 변환
        # 반환 형식 맞추기
        unique_hull = list(set(map(tuple, hull)))
        return [list(point) for point in unique_hull]

