import math
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 각 query와 point의 거리 구하기
        # query의 r보다 작으면 내부에 point 있는 것임
        answer = [0 for _ in queries]
        for i, (x_c, y_c, r) in enumerate(queries):
            for x_i, y_i in points:
                if math.sqrt((x_c-x_i)**2 + (y_c-y_i)**2) <= r:
                    answer[i] += 1
        
        return answer
            
