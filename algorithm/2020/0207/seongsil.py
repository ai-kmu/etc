# 답은 잘나오는데 왜 런타임 에러가 뜨는지 몰겠음다

MAX = 1001

def pre_solve(dp, first_color,num_of_house):
    for j in range(num_of_house):
        if j == first_color:
            dp[0][j] = cost[0][j]
        else:
            dp[0][j] = MAX

def solve(num_of_house, cost):
    min_ = 1001
    for i in range(3): #첫번째 집 색 고정
        dp = [[-1]*3 for _ in range(num_of_house)]
        pre_solve(dp,i,num_of_house)        
        for j in range(1,num_of_house):
            dp[j][0] = cost[j][0] + min(dp[j-1][1], dp[j-1][2])
            dp[j][1] = cost[j][1] + min(dp[j-1][0], dp[j-1][2])
            dp[j][2] = cost[j][2] + min(dp[j-1][0], dp[j-1][1])
            
        dp[num_of_house-1][i] = MAX

        if min_ > min(dp[num_of_house-1]):
            min_ = min(dp[num_of_house-1])

    return min_


num_of_house = int(input())
cost = []
for n in range(num_of_house):
    temp = list(map(int, input().split()))
    cost.append(temp)

print(solve(num_of_house, cost))
