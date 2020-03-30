# 14. 백준 - 동전

# 값 받아오기
total_coin_cnt, total_cost = map(int, input().split())

# 전체 가능한 경우와 해당하는 경우의 수 저장
coin_category = []
possible_comb = []
for i in range(total_coin_cnt):
    cost = int(input())
    coin_category.append(cost)
    if cost <= total_cost:
        possible_comb.append(cost)

# 내림차순 저장
possible_comb.sort(reverse=True)
# print(possible_comb)

# 동전의 개수 세기(해당하는 경우의 수에 한해서)
coin_cnt = 0
for i in range(len(possible_comb)):
    if total_cost == 0:
        break
    if possible_comb[i] > total_cost:
        continue
    coin_cnt += total_cost // possible_comb[i]
    total_cost %= possible_comb[i]

print(coin_cnt)