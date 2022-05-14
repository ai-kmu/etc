from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        # 예외처리: 점이 두 개 이하면 그게 답임
        if len(points) <= 2:
            return len(points)
        
        # slope, intercept를 key로 하고
        # 그런 직선 위의 point들의 set을 value로 하는 dictionary
        lines = defaultdict(set)

        # 이중 for문: 모든 case에 대해서 직선 만들어 보기
        for i, point1 in enumerate(points):
            for point2 in points[i+1:]:
                # 직선 만들기
                ## x 값이 같으면 기울기 = 무한
                ## -> slope=None, intercept=x값
                if point1[0] == point2[0]:
                    slope = None
                    intercept = point1[0]
                ## 이외 - 기본적인 직선의 방정식
                else:
                    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
                    intercept = point1[1] - slope * point1[0]
                
                # dictionary update
                lines[(slope, intercept)].add(tuple(point1))
                lines[(slope, intercept)].add(tuple(point2))
        
        # 정답 계산
        ans = 0
        for line in lines:
            ans = max(len(lines[line]), ans)

        return ans
