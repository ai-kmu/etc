__author__ = 'judepark'

coin_count, total_cost = map(int, input().split())

coins = []

for i in range(coin_count):
    cost = int(input())

    # total_cost 보다 큰 cost 는 저장할 필요 없음
    if cost <= total_cost:
        coins.append(cost)


answer = 0

# 가장 큰 값부터 시작
for i in range(len(coins), 0, -1):
    answer += int(total_cost / coins[i - 1]) # 가장 큰 값의 동전을 몇 번을 뺐는지?
    total_cost %= coins[i - 1]  # 빼고 남은 값 갱신

print(answer)
