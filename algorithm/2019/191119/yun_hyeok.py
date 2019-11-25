N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]


def solution(coins):
    answer = 0
    t = K
    for coin in reversed(coins):
        if t < coin:
            continue
        n = t // coin
        answer += n
        t = t - coin * n
    return answer


print(solution(coins))
