# test case는 통과
# [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]] case 에서 예측 실패
# 시도 방법은 두 점으로 직선의 방정식의 파라미터 a, b(y = ax + b) 를 구해서 같은 점들 개수 세기 
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = {}
        len_num = len(points)
        if len_num < 3:
            return len_num

        # 중복 금지 반복문
        for i in range(len_num):
            for j in range(i+1, len_num):      
                # 기울기, 편향 구하기
                delta_x = points[i][0] - points[j][0]
                delta_y = points[i][1] - points[j][1]
                # zero div가 아닌 경우(기울기가 0이 아닌 경우)
                if (delta_x !=0):
                    slope = delta_y/delta_x
                    bias = points[i][1] - slope * points[i][0]
                    param = (slope, bias)       
                    
                    # 딕셔너리에 param을 키로 설정하고 각 점을 넣는다 => 추후 set을 통해 중복제거해서 개수파악
                    if param not in result:
                        result[param] = []
                        result[param].append(points[i])
                        result[param].append(points[j])
                    else:
                        result[param].append(points[i])
                        result[param].append(points[j])
                # zero div인 경우 (기울기가 0인 경우)
                else:
                    slope = float('inf')
                    bias = points[i][0]
                    param = (slope, bias)
                    
                    if param not in result:
                        result[param] = []
                    
                    result[param].append(points[i])
                    result[param].append(points[j])
        
        aws = []
        
        # 같은 param을 가지는 점들의 중복 제거
        for i in result.keys():
            line_point = set(map(tuple, result[i]))
            aws.append(len(line_point))
        if aws != []:
            return max(aws)
        else:
            return 1
