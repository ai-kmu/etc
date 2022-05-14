from collections import defaultdict

#각 점에서 자신과 기울기가 같은 점들의 개수를 세어서 해결
#개수를 세기 위하여 dictionary 사용
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = 0
        
        #점이 하나만 있을때의 예외처리
        if len(points) == 1:
            return 1
        
        # x1-x2 / y1-y2를 하여 기울기를 계산
        # 계산한 기울기 값을 key로하여 dictionary에 저장
        for i in range(len(points) - 1):
            slope_dict = defaultdict(int)
            for j in range(i + 1, len(points)):
                #y1-y2가 0일때 즉 0이 분모일 때 나눗셈이 불가
                #따라서 따로 처리함
                if points[i][1] - points[j][1] == 0:
                    #아직 dict 값이 0일때에는 자기 자신 + 다른 점 추가
                    #그 후에는 다른 점만 추가
                    if slope_dict['inf'] == 0:
                        slope_dict['inf'] += 2
                    else:
                        slope_dict['inf'] += 1
                        
                #정상적으로 기울기 값을 구해서 진행
                else:          
                    slope = (points[i][0] - points[j][0]) / (points[i][1] - points[j][1])
                
                    if slope_dict[slope] == 0:
                        slope_dict[slope] += 2
                    else:
                        slope_dict[slope] += 1
                
                #max함수를 이용해서 점이 가장 많이 포함된 선을 찾고 점의 개수를 구함
                max_slope = max(slope_dict, key = slope_dict.get)
                max_points = max(max_points, slope_dict[max_slope])
        
        return max_points
