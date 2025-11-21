class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        def check_rectangle(rect):
            nonlocal vertices
            for vertex in rect:
                if vertex not in vertices:
                    vertices.add(vertex)
                else:
                    vertices.remove(vertex)
            
            return True

        vertices = set()
        area = 0
        
        for rect in rectangles:
            area += (rect[2] - rect[0]) * (rect[3] - rect[1])
            if not check_rectangle([(rect[0], rect[1]), (rect[0], rect[3]), (rect[2], rect[3]), (rect[2], rect[1])]):
                return False
        
        if len(vertices) != 4:
            return False
        
        x1, y1 = min(vertices)
        x2, y2 = max(vertices)
        return area == (x2 - x1) * (y2 - y1)
