num, sum = map(int, input().split())
coins = [int(input()) for i in range(num)]
coins.sort(reverse=True)
    
def solution(coins):
    answer = 0
    n = 0
    tmp = sum
    
    for coin in coins:
        if tmp < coin:
            continue
        n, tmp = tmp//coin, tmp%coin
        answer += n

    return answer

print(solution(coins))
