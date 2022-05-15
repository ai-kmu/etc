# 테스트 케이스 다 통과 못함 (오답)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        answer = 0
        
        # 길이가 1 이면 1 return
        if len(points) == 1:
            return 1
        
        for i in range(len(points)):
            overlap = 0
            slope = 0
            max_point = {'inf': 0}

            for j in range(i+1, len(points)):
                
                # 같은 점인 경우
                if points[i][1] == points[j][1] and points[i][0] == points[j][0]:
                    overlap += 1
                
                else:
                    # 두 점의 x값이 다른 경우
                    if points[j][0] != points[i][0]:
                        slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                        
                        if slope not in max_point.keys():
                            max_point[slope] = 2
                        else:
                            max_point[slope] += 1
                        
                    # 두 점의 x 값은 같고 y 값은 다른 경우는 기울기가 무한대
                    if points[i][0] == points[j][0] and points[i][1] != points[j][1]:
                        max_point['inf'] += 1
                
                answer = max(answer, max(max_point.values()) + overlap)
            
        return answer
