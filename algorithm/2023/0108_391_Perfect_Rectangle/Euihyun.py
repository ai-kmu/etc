# 수정중
# 넓이 부분만 생각해서 추가하면 될거 같은데..
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # 체크포인트 설정
        check_point = set()
        
        for i in rectangles :
            # 각 점들 지정
            x, y, a, b = i[0], i[1], i[2], i[3] 
            # 넓이 지정
            area = (a-x) * (b-y)
            
            # 각 꼭지점 [y, x], [y, a], [b, x], [b, a]
            for point in [(y,x), (y,a), (b,x), (b,a)] : 
                # 꼭지점 체크
                if point in check_point:
                    check_point.remove(point)
                else:
                    check_point.add(point)

        # 4개가 아니면 겹치는거로 False
        if len(check_point) != 4 :
            return False

        
        
        
                

