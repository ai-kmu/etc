# 희안하게 풀었음...

# 값을 하나 잡고, times의 첫 숫자와 곱함
# 그 숫자에서의 수용인원 수가 n보다 크면 값을 줄이고 작으면 늘림
import math
def solution(n, times):
    times.sort()
    left = 0
    right = n
    mid = math.floor((left + right)/2)
    cnt = 0
    v = times[0]
    # 업데이트 여부 확인 변수
    preMid = -1
    while(preMid != mid):
        preMid = mid
        num = mid * v
        cnt = 0
        for time in times:
            cnt += math.floor(num / time)
        if cnt >= n:
            right = mid
        else:
            left = mid
        mid = math.floor((left + right)/2)
    # lower bound를 찾았으니 threshold 찾으려 brute force를 쓰려 했으나 역시 느리다
    # 지수적으로 범위를 줄이고 적당한 위치에서 brute force
    val = mid * v
    preval = -1001
    step = 0
    while abs(preval - val) > 1000:
        step = 0
        while cnt < n:
            val += math.pow(2, step)
            step += 1
            cnt = 0
            for time in times:
                cnt += math.floor(val / time)
        preval = val
        step -= 1
        val -= math.pow(2, step)
        cnt = 0
    while cnt < n:
        val += 1
        cnt = 0
        for time in times:
            cnt += math.floor(val / time)
    return val
            
    
