class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # wrong case
    
        # check area
        xm, ym, amax, bmax = float("inf"), float("inf"), float("-inf"), float("-inf")
        for _ in rectangles:
            x, y, a, b = _[0], _[1], _[2], _[3]
            if x < xm:
                xm = x
            if y < ym:
                ym = y
            if a > amax:
                amax = a
            if b > bmax:
                bmax = b
        
        print(xm,ym,amax,bmax)
