N, money = map(int, input().split())
coin_list = []

#N만큼 동전 종류 추가
for i in range(N):
    coin = int(input())
    coin_list.append(coin)

# 내림차순 정렬
coin_list.sort(reverse=True)

coin_num = 0
for coin in coin_list:
    # 현재 동전으로 필요한 돈이 나눠지는 경우 -> 동전수를 몫만큼 더하고 돈에서 빼준다
    if(money // coin != 0):
        coin_num += money//coin
        money %= coin

print(coin_num)
