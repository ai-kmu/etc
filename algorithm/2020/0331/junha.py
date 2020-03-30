# make variable 
coins = []
answer = 0

# bring the inputs
n, k = map(int, input().split())
for i in range(n):
    coins.append(int(input()))

# calculate a number of coins to need
for i in range(n-1, -1, -1):
    if k >= coins[i]:
        num, k = divmod(k, coins[i])
        answer += num
    elif k == 0 :
        break

print(answer)
