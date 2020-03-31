num, sum = map(int, input().split())
coins = [int(input()) for i in range(num)]
coins.sort(reverse=True)  #동전 개수의 최솟값 구해야하니 큰 동전부터
    
def solution(coins):
    answer = 0
    n = 0
    tmp = sum
    
    for coin in coins:
        if tmp < coin:
            continue
        n, tmp = tmp//coin, tmp%coin  # 최대 사용할 수 있는 동전 개수는 n에, 나머지 값은 tmp에
        answer += n

    return answer

print(solution(coins))
