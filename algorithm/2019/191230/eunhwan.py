D, K = map(int, input().split(' '))

a, b = 1, 1

# first day, second day
for i in range(3, D):
    t = b
    b = a + b
    a = t

s, i = False, 1

while True:
    j = 1
    while True:
        r = a * i + b * j
        if r > K:
            break
        elif r == K:
            s = True
            break
        j += 1
    if s:
        break
    i += 1

print(i)
print(j)
