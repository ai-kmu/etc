import math

def solution(brown, yellow):
    mulxy = brown + yellow
    plxy = (brown + 4) / 2
    mixy = math.sqrt(plxy**2 - 4*mulxy)
    y = (plxy - mixy) / 2
    x = plxy - y
    return [x, y]
