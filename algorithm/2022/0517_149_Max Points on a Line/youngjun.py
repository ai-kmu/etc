class Solution(object):
    def maxPoints(self, points):
        # 기울기와 intercept를 구하고, 이를 반환하는 함수를 만듦
        # 기울기를 구할 때, x 변화량이 0일경우 ZeroDivisionError가 발생, 예외처리를 해줘야 함
        def cal_grad(p1, p2):
            delta_x = p1[0] - p2[0]
            delta_y = p1[1] - p2[1]
            try:
                if delta_y == 0:
                    grad = 0
                else:
                    grad = delta_y / delta_x
                y_intercept = p1[1] - (grad * p1[0])
                return str(round(grad, 8)) + ", " + str(round(y_intercept, 8))
            except ZeroDivisionError:
                grad = float('inf')
                x_intercept = p1[0]
                return str(round(grad, 8)) + ", " + str(round(x_intercept, 8))
                
        # points가 1일 경우, 1을 반환
        if len(points) == 1: # 예외처리
            return 1
        
        # 기울기에서 생성될 수 있는 점이 1 이상씩 있으므로, 딕셔너리를 1로 초기화
        grad_dict = defaultdict(lambda:1)
        
        # 모든 점을 돌면서 key에 1씩 추가
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                grad_key = cal_grad(points[i], points[j])
                grad_dict[grad_key] += 1

        # n(n-1)/2 = k
        # n^2 - n + 2K = 0
        # n = (1 + root(1 + 8k)) / 2           
        return (1 + int((1 + 8 * max(grad_dict.values())) ** 0.5)) // 2
