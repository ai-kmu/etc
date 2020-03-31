N, K = map(int, input().split())
coin_val = [int(input()) for i in range(N)]
count = 0
signal = False

while True:
    for i in range(N-1,-1,-1):    # 큰 동전부터 작은동전으로 반복
        if K < coin_val[i]:       # K가 더 작은경우 스킵
            continue
        count += K // coin_val[i] # 몇개 쓸수있는지 계산
        K %= coin_val[i]          # K에서 빼줌
        if K == 0:                # K가 0이면 끝남
            signal = True
            break
        N = i
        break
    if signal:
        break
print(count)
