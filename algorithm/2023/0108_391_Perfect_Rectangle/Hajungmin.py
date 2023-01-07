lass Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
      
        # 좌표를 이용하여 4개의 사각형 좌표를 저장할 딕셔너리
        # 총 영역을 계산하는 total_area를 선언
        points = dict()
        total_area = 0

        # 각 포인트를 계산하여 딕셔너리에 좌표들이 등장하는 횟수를 셈
        for point in rectangles:
            x1, y1, x2, y2 = point
            curr_area = int(abs(x1 - x2) * abs(y2 - y1))
            total_area += curr_area

            point1 = (x1, y1)
            if point1 in points:
                points[point1] += 1
            else:
                points[point1] = 1

            point2 = (x1, y2)

            if point2 in points:
                points[point2] += 1
            else:
                points[point2] = 1

            point3 = (x2, y1)
            if point3 in points:
                points[point3] += 1
            else:
                points[point3] = 1

            point4 = (x2, y2)
            if point4 in points:
                points[point4] += 1
            else:
                points[point4] = 1
        
        res = []
        # 이후 좌표들이 등장하는 수가 짝수면 사각형이 맞춰져서 인접해 있는 것이므로 제거
        # 홀수라면 남겨둠
        for i in points:
            if points[i] % 2 != 0:
                res.append(i)
        
        # 이 때 남겨진 좌표는 사각형이어야하므로 4개
        # 만약 4개가 아니면 False 반환
        if len(res) != 4: return False
        
        # 결과로 나온 좌표들을 정렬 후 x1, y1, x2, y2를 계산해서
        # 총 영역 계산
        res = sorted(res)

        x1, y1 = res[0]
        x2, y2 = res[-1]
        # 만약 총 영역이 각 사각형의 합과 같다면 true, 아니라면 false
        if int(abs(x2-x1) * abs(y2-y1)) == total_area: return True
        else: return False
