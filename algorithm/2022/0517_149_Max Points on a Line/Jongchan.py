'''
모든 점을 조사하며, 가능한 기울기를 모두 조사
y = ax + b -> (x1,y1), (x2,y2)에서 a와 b를 구하고 a b 쌍을 key값으로 딕셔너리 생성
딕셔너리의 value 중 가장 큰 값이 정답
'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: # 예외처리
            return 1
        
        grad = dict() # 딕셔너리 선언
        for i in range(0,len(points)):
            grad_ = dict() # 임시 딕셔너리 -> 같은 기울기가 여러번 나올 수 있기 때문
            for j in range(0, len(points)):
                if i != j:
                    m=""
                    if points[i][0] - points[j][0] == 0:
                        m = "x = " + str(points[i][0])
                    elif points[i][1] - points[j][1] == 0:
                        m = "y = " + str(points[i][1])
                    else:
                        a = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                        b = points[i][1] - a * points[i][0]
                        m = str(round(a, 8)) + " " + str(round(b, 8)) # 나눗셈 연산시 정확도 문제 발생, 반올림으로 해결

                    if m not in grad_:
                        grad_[m] = 1
                        
                        
            for g_k in grad_.keys(): # grad 딕셔너리 업데이트
                if g_k in grad:
                    grad[g_k] += 1
                else:
                    grad[g_k] = 1
        
        return max(grad.values())
