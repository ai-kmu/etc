#K를 표현할 수 있는 최소금액만들기

N, K = map(int, input().split())
money = [int(input()) for i in range(N)]

answer = 0
curr_money_i = N-1
# 같은 동전 값을 써도 되기 때문에 coin_count 추가
coin_count = 0

while K > 0:
    # 내림차순으로 움직이면서 K보다 작은 제일 큰 동전을 찾음.
    if K - money[curr_money_i] < 0:
        curr_money_i -= 1
        continue
    else:
        # 제일 큰 동전을 찾으면 coin의 개수를 update시켜줌.
        coin_count = K // money[curr_money_i]
        # K도 update한다.
        K -= money[curr_money_i]*coin_count
        answer += coin_count

print(answer)
