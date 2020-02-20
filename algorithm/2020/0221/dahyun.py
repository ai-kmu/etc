
N, K = map(int, input().split())

t = 0

if N < K:  # 수빈 < 동생 일 때
    while 2*N <= K:
        N = 2*N
        
    if N != K:
        if K % 2 == 0:  # K가 짝수면
            t += min(N - K/2, K - N)
        else:           # K가 홀수면
            t += min(N - (K+1)/2 + 1, K - N)
            
elif N > K:  # 수빈 > 동생 일 때
    t = N - K
    
print(int(t))

