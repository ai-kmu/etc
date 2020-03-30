# A_{1} = 1, i ≥ 2인 경우에 A_{i}는 A_{i-1}의 배수
# 라는 조건이 없었다면 DP를 했어야 했으나
# 이 조건으로 인해 greedy 하게 푸는 것이 가능해진다.
# 조건을 조금 풀어서 해석하자면
# 작은 동전들을 여러번 조합하면 큰 동전을 무조건 만들 수 있다는 뜻이다.
# 따라서 큰 동전을 택할 수 있는 상황이라면 큰 동전을 택해야한다.

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0
for i in range(len(coins), 0, -1):
    count += int(K / coins[i - 1])
    K %= coins[i-1]

print(count)
