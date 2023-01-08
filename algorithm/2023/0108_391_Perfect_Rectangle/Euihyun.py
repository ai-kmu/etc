수정수정중
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # 체크포인트 설정
        check_point = set()
        total_area = 0
        for i in rectangles :
            # 각 점들 지정
            x, y, a, b = i[0], i[1], i[2], i[3] 
            # 전체 넓이 합
            total_area += (a-x) * (b-y)

            # 각 꼭지점 [x, y], [x, b], [a, y], [a, b]
            for point in [(x,y), (x,b), (a,y), (a,b)] : 
                # 꼭지점 체크
                if point in check_point:
                    check_point.remove(point)
                else:
                    check_point.add(point)

        # 4개가 아니면 겹치는거로 False
        if len(check_point) != 4 :
            return False

        return total_area == ((max(rectangles[2])-min(rectangles[0]))*(max(rectangles[3]) - min(rectangles[1])))
