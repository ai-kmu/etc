import math

# 간단한 다항식을 응용해 문제를 풀 수 있다.
def solution(brown, yellow):
    # x*y = brown + yellow
    mulxy = brown + yellow
    # x + y = (brown + 4) / 2라면,
    plxy = (brown + 4) / 2
    # x - y는 (x + y)^2 - 4xy의 제곱근이다.
    mixy = math.sqrt(plxy**2 - 4*mulxy)
    # 이렇게 (x + y)와 (x - y)를 구한 후, 둘을 빼준 후 2로 나누면 y를 구할 수 있다.
    y = (plxy - mixy) / 2
    # x를 구해준다.
    x = plxy - y
    return [x, y]
