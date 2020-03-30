############ 입력 받기 #############################
# numOfCoins : 동전 종류의 개수 / sumOfCoins : 입력받은 동전들로 만들어야 하는 금액
numOfCoins, sumOfCoins = map(int, input().split())
coins = [int(input()) for i in range(numOfCoins)]

###### 큰 수 부터 계산하기 위해 내림차순으로 정렬 ######
coins.sort(reverse=True)

###### greedy algorithm #####
def solution(coins):
    # answer : 총 사용한 동전의 개수를 담을 변수
    answer = 0 
    # temp : 구해야하는 총 금액을 담을 변수
    temp = sumOfCoins
  
    for coin in coins:
        # 동전이 구해야 하는 금액보다 크면 continue
        if (temp < coin):
            continue
        # 동전이 구해야 하는 금액보다 작으면
        ## 동전을 총 몇개 사용할 수 있는 지 구하고 answer에 더해줌
        n = temp // coin
        answer += n
        ## 사용한 동전의 금액만큼 빼줌
        temp = temp - coin*n
    
    return answer

print(solution(coins))
