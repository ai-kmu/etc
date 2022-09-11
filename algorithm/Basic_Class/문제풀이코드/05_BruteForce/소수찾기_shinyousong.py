import math
import itertools
def solution(numbers):
    # 마킹
    check = []
    # 소수판별
    def prime(x):
        if x == 1 or x == 0:
            return 0
        if x in check:
            return 0
        for i in range(2, int(math.sqrt(x))+1):
            if x%i == 0:
                return 0
        check.append(x)
        return 1
    
    # 찢기
    numbers = [numbers[i] for i in range(len(numbers))]
    cnt = 0
    for i in range(1, len(numbers)+1):
        t = itertools.permutations(numbers, i)
        # 경우를 빼옴
        for t2 in t:
            # 숫자로 만듬
            tmp = ""
            for s in t2:
                tmp += s
            cnt += prime(int(tmp))
    answer = cnt
    return answer
