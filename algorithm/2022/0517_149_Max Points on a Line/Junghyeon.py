from collections import Counter


class Solution:
    '''
    모든 두 점 사이의 기울기와 절편 값을 구하고 딕셔너리로 각각 모든 경우의 개수를 구한다.
    '''
    def maxPoints(self, points: List[List[int]]) -> int:
        # 기울기와 절편 값을 구하는 함수
        def get_grad(p1, p2):
            try:
                if p2[1] - p1[1] == 0:
                    grad = 0
                else:
                    grad = (p2[1] - p1[1]) / (p2[0] - p1[0])
                y_intercept = p1[1] - (grad * p1[0])
            # x 값이 같을 때 -> 기울기는 무한대이므로 별도의 예외 처리
            except ZeroDivisionError:
                grad = float('inf')
                x_intercept = p1[0]
                # 부동소수점 문제 해결을 위한 반올림
                return str(round(grad, 10)) + ", " + str(round(x_intercept, 10))
            # 부동소수점 문제 해결을 위한 반올림
            return str(round(grad, 10)) + ", " + str(round(y_intercept, 10))

        if len(points) == 1:
            return 1
        
        grad_dict = dict()

        # 모든 점을 비교하면서 딕셔너리에 추가하고, 개수를 구한다.
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                key = get_grad(points[i], points[j])
                if key in grad_dict:
                    grad_dict[key] += 1
                else:
                    grad_dict[key] = 1

        # 이때 구한 최댓값은 C(n, 2)를 해서 나온 값이 되기 때문에 n을 추가적으로 구해야 한다.
        cnt = 2 * Counter(grad_dict).most_common(1)[0][1]

        # n을 1부터 증가시켜서 n*(n+1)을 만족시키면 결과값 리턴
        n = 1
        while n*(n+1) != cnt:
            n += 1

        return n+1
