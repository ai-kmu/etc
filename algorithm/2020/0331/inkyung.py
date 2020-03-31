N, K = map(int, input().split())
coin_val = [int(input()) for i in range(N)]

coin_val = sorted(coin_val, reverse=True)
idx, num, val = 0, 0, 0
while K > 0:
    if K < coin_val[idx]:
        idx += 1
        continue
    else:
        num = K // coin_val[idx]
        K -= coin_val[idx] * num
        val += num
        idx += 1

