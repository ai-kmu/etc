'''
출발지 -> 도착지로 갈때 최댓값을 dp 테이블에 업데이트
이후 최댓값의 경로에 있는 체리를 지우고 도착지 -> 출발지로 가면서 dp 테이블을 업데이트하려고 시도했으나 구현 실패
'''
dp = [[0] * len(grid) for _ in range(len(grid))]

# col = 0인경우 사용할 flag
flag1 = True
# row = 0인경우 사용할 flag
flag2 = True
tmp_sum = 0
result = 0

# row와 col이 0일때 dp 테이블 업데이트
for i in range(len(grid)):
    for j in range(len(grid)):
        if i == 0 and flag1:
            if grid[i][j] == -1:
                flag1 = False
                continue
            dp[i][j] = sum(grid[i][:j+1])
        if j == 0 and flag2:
            if grid[i][j] == -1:
                flag2 = False
                continue
            elif grid[i][j] == 1:
                tmp_sum += 1
                dp[i][j] = tmp_sum
            else:
                dp[i][j] = dp[i-1][j]

# 매 위치마다 위에서 오는 것과 왼쪽에서 오는 것 중 최댓값 저장
for i in range(1, len(grid)):
    for j in range(1, len(grid)):
        if grid[i][j] == -1:
            continue
        if dp[i-1][j] > dp[i][j-1]:
            grid[i-1][j] = 0
            dp[i][j] = dp[i-1][j]
        else:
            grid[i][j-1] = 0
            dp[i][j] = dp[i][j-1]
        if grid[i][j] == 1:
            dp[i][j] += 1

result += dp[-1][-1]
