from itertools import combinations

class Solution(object):
    def maxPoints(self, points):
        
        # y = a * x + b
        # y = (y_1 - y_2) / (x_1 - x_2) * x + b
        # y * (x_1 - x_2) = (y_1 - y_2) * x + b * (x_1 - x_2)
        # x 와 y 에 x_1과 y_!을 대입하여 b를 알아낸다.
        # a와 b를 알아내어 같은 직선안에있는 점의 수를 구한다.
        
        # 길이가 1일때 예외처리
        if len(points) == 1:
            return 1
        
        pair_list = list(combinations(points,2)) # [(x_1, y_1),(x_2, y_2)]
        
        # a_list a_coef, b_coef, c_coef, d_coef 구해서 set하기
        answer = 0
        for i in range(len(pair_list)):
            
            y_coef = (pair_list[i][0][1]-pair_list[i][1][1])
            x_coef = (pair_list[i][0][0]-pair_list[i][1][0])            
            b_dot_b_coef = pair_list[i][0][1]*x_coef - y_coef*(pair_list[i][0][0])

            i = 0
            tmp_answer = 0
            
            for point in points:
                if (point[1])*x_coef ==  y_coef*(point[0]) + b_dot_b_coef:
                    tmp_answer += 1
            answer = max(tmp_answer,answer)
            
        return answer
