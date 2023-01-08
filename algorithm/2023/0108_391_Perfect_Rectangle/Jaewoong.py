# 풀이실패...
class Solution:
    hs = set()
    def build_r_map(self, rectangles):
        total_area, pt = 0, defaultdict(int)
        for r in rectangles:
            # 영역 설정
            top_left = (r[0], r[1])
            top_right = (r[0], r[3])
            bottom_left = (r[2], r[1])
            bottom_right = (r[2], r[3])
            for i in [top_left, top_right, bottom_left, bottom_right]:
                #if i not in hs:
                #지정 특정영역 벗어나면 false
