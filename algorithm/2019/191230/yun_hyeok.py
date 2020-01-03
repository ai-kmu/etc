n, k = map(int, input().split())

fibo = [None] * n
fibo[0] = 1
fibo[1] = 1

while True:
    for i in range(2, n):
        fibo[i] = fibo[i-2] + fibo[i-1]
        if fibo[i] >= k:
            break
    if fibo[-1] == k:
        print(fibo[0])
        print(fibo[1])
        exit()
    if fibo[0] < fibo[1]:
        fibo[0] += 1
    else:
        fibo[1] += 1
        fibo[0] = 1
    # print(f"fibo[0]: {fibo[0]}, fibo[1]: {fibo[1]}")
