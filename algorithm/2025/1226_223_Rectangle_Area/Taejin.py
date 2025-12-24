class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        # 겹치는 부분 계산
        # 예시 그림보면 우상단 = (ax2, ay2)와 (bx2, by2) 최소
        # 좌상단 = (ax1, ay1)와 (bx1, by1) 최대
        # 안겹치면 가로 또는 세로 길이 음수나와서 max로 처리
        area3 = (max((min(ay2, by2) - max(ay1, by1)),0) * max((min(ax2, bx2) - max(ax1, bx1)),0)) 

        return area1 + area2 - area3
