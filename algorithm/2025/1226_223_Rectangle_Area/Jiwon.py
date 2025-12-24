# 솔루션 참고
class Solution:
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) -> int:
        
        int_area = (max((min(ay2, by2)-max(ay1, by1)),0)*               #  int_area is the area of the rectangles' 
                    max((min(ax2, bx2)-max(ax1, bx1)),0))               #  intersection. If no intersection, int_area == 0
                       
        return ((ax2-ax1)*(ay2-ay1) +                                   #  area of rectangle A +
                (bx2-bx1)*(by2-by1) -                                   #  area of rectangle B -
                int_area              )                                 #  area of the intersection, if any
