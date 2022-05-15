class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        D = dict()
        
        # points가 하나일 경우 기본값 1 처리
        if len(points) == 1: 
            return 1
        
        for i in range(len(points)):
            d = dict()

            for j in range(len(points)): 
                if i == j: continue  
                (x1, y1) = points[i]
                (x2, y2) = points[j]

                # division by zero 오류 발생해서
                # 기울기 0 , 90 , 이외의 경우 계산 
                if x2 - x1 == 0: 
                    slope = 0
                elif y2 - y1 == 0: 
                    slope = 90
                else: 
                    slope = (y2 - y1) / (x2 - x1)

                # 같은 기울기면 점 추가
                if slope not in d:  # 같은 기울기가 아니라면, 기본값 2
                    d[slope] = 2
                else:  # 같은 기울기라면 추가
                    d[slope] += 1
            D[i] = d
        answer = 0
        
        # 동일한 기울기를 가진 값들 가장 많은 것 ->  answer로 return
        for val1 in D.values():
            for val2 in val1.values():
                answer = max(answer, val2)
        return answer
        
        
