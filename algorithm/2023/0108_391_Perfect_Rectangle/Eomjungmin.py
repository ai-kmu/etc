class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        recs = {}

        total_S = 0 # 전체 사각형 넓이
        for rec in rectangles:
            x1, y1, x2, y2 = rec
            # 현재 사각형의 4개 점 저장
            point1 = (x1, y1)
            point2 = (x1, y2)
            point3 = (x2, y1)
            point4 = (x2, y2)
             
            # 현재 사각형 넓이 계산 후 total_S에 저장
            cur_S = abs(x2 - x1) * abs(y2 - y1)
            total_S += cur_S
            
            # 각 포인트마다 개수 저장하는데 2개로 겹치는 순간 0으로 바꿈
            if point1 in recs:
                recs[point1] += 1
                if recs[point1] % 2 == 0:
                   recs[point1] = 0 
            else:
                recs[point1] = 1

            if point2 in recs:
                recs[point2] += 1
                if recs[point2] % 2 == 0:
                   recs[point2] = 0
            else:
                recs[point2] = 1

            if point3 in recs:
                recs[point3] += 1
                if recs[point3] % 2 == 0:
                   recs[point3] = 0
            else:
                recs[point3] = 1

            if point4 in recs:
                recs[point4] += 1
                if recs[point4] % 2 == 0:
                   recs[point4] = 0
            else:
                recs[point4] = 1
        
        # recs에서 개수가 0인 것은 겹쳤다는 의미이므로 겹친 점들은 빼고 나머지 점들 따로 저장
        final_points = []
        for p in recs:
            if recs[p] != 0:
                final_points.append(p)
        
        # 최종으로 남은 점은 반드시 4개여야 함
        if len(final_points) != 4:
            return False

        final_points.sort() # 면적 계산을 위해 final_points 정렬
        
        # total_S와 남은 4개 점을 이용한 사각형 넓이가 일치하면 True, 아니면 False 
        if total_S == abs(final_points[0][0] - final_points[3][0]) * abs(final_points[0][1] - final_points[1][1]):
            return True
        else:
            return False
