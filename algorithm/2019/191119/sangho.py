n, k = map(int, input().split())

m = [int(input()) for x in range(n)]
count = 0

for i in range(n):
    mon  = m[n-1-i]
    if k >= mon :
        count += k//mon 
        k %= mon
print(count)    
