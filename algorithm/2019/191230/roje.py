D, K = map(int, input().split())

def fibo(n):
  if n <= 1:
    return 1
  return fibo(n-1) + fibo(n-2)

coefA = fibo(D-3)
coefB = fibo(D-2)

for A in range(K//coefA):
    for B in range(K//coefB):
        answer = coefA*A + coefB*B
        if answer == K:
            if A < B:
                print(A)
                print(B)
                break
