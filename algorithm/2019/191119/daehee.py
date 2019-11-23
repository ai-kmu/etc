N, K = map(int, input().split())
coin_val = [int(input()) for i in range(N)]
count = 0
signal = False

while True:
    for i in range(N-1,-1,-1):
        if K < coin_val[i]:
            continue
        count += K // coin_val[i]
        K %= coin_val[i]
        if K == 0:
            signal = True
            break
        break
    if signal:
        break
print(count)