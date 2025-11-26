class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        hs = set()
        area = 0
        for rec in rectangles:
            top_left = (rec[0], rec[1])
            top_right = (rec[0], rec[3])
            bottom_left = (rec[2], rec[1])
            bottom_right = (rec[2], rec[3])
            area += (rec[2] - rec[0]) * (rec[3] - rec[1])
            for i in [top_left, top_right, bottom_left, bottom_right]:
                if i not in hs:
                    hs.add(i)
                else:
                    hs.remove(i)
        if len(hs) != 4:
            return False
        hs = sorted(hs)
        first = hs.pop(0)
        last = hs.pop()
        return area == (last[0] - first[0]) * (last[1] - first[1])
        
