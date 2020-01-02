def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

#D는 할머니가 넘어온 날, K는 호랑이에게 준 떡의 개수
D, K = map(int, input().split(' '))

x, y = fibo(D - 3), fibo(D - 2)
lst = []

j, boo = 1, False
while boo == False:
    i = 1
    while i <= j:
        if (x * i) + (y * j) == K:
            lst.append([i, j])
            boo = True
            break
        i += 1
    if boo == True:
        break
    j += 1

num1, num2 = min(lst[0]), max(lst[0])

print(num1)
print(num2)
