from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # points가 주어지면 가장 많은 점을 포함하는 라인을 만들었을 때 점의 개수를 구해라
        # 포인트 페어의 기울기를 구하고 그 포인트들을 제외한 점의 개수를 구해라.
        # 기울기는 set에 저장
        if len(points) < 2:
            return 1
        gradient_set = defaultdict(set)
        
        for x1, y1 in points: # 겹치지 않는 모든 pair 검사
            for x2, y2 in points[1:]:
                # 기울기 구하기
                gradient = 0
                if x1 < x2:
                    gradient = (y2 - y1) / (x2 - x1)
                elif x1 > x2:
                    gradient = (y1 - y2) / (x1 - x2)
                else:
                    gradient = float('inf')

                # y = m*(x-x1) + y1
                # y == 0일 때 x0가 같다면, 같은 직선에 있는 것임
                if gradient == 0: # 가로 직선
                    x0 = y1
                elif gradient == float('inf'): # 세로 직선
                    x0 = x1
                else:
                    x0 = (-y1 / gradient) + x1
                
                # y=0일 때, x의 값을 키로 두기 (가로 직선일 때는 y값 키로 두기)
                gradient_set[(gradient, x0)].add((x1, y1))
                gradient_set[(gradient, x0)].add((x2, y2))
        
        answer = 0
        for ele_arr in gradient_set.values():
            answer = max(answer, len(ele_arr))
        
        return answer
