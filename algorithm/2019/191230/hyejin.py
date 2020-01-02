
D, K = map(int, input().split())

# 점화식 이용
a1_pre = 0
a1_current = 1
a2_pre = 1
a2_current = 1
i = 3
while i != D:
    a1_pre, a1_current = a1_current, a1_pre
    a1_current += a1_pre

    a2_pre, a2_current = a2_current, a2_pre
    a2_current += a2_pre

    i += 1

i = 1
state = False
while True:
    j = 1
    while True:
        check = a1_current * i + a2_current * j
        if check > K:
            break
        elif check == K:
            state = True
            break
        j += 1
    if state:
        break
    i += 1
print(i)
print(j)

