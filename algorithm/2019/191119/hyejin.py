#K를 표현할 수 있는 최소금액만들기

N, K = map(int, input().split())
money = [int(input()) for i in range(N)]

answer = 0
curr_money_i = N-1
# 같은 동전 값을 써도 되기 때문에 coin_count 추가
coin_count = 0

while K > 0:
    if K - money[curr_money_i] < 0:
        curr_money_i -= 1
        continue
    else:
        coin_count = K // money[curr_money_i]
        K -= money[curr_money_i]*coin_count
        answer += coin_count

print(answer)