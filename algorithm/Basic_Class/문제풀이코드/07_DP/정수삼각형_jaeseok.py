def solution(triangle):
    # dp 테이블 초기화
    dp = []
    for i in range(1, len(triangle) + 1):
        dp.append([0] * i)
    dp[0][0] = triangle[0][0]
    # 외곽 부분 계산
    for i in range(1, len(triangle)):
        dp[i][0] = dp[i - 1][0] + triangle[i][0]
        dp[i][-1] = dp[i - 1][-1] + triangle[i][-1]
    # 나머지 부분 계산
    for i in range(2, len(triangle) + 1):
        for j in range(i - 2):
            dp[i - 1][j + 1] = max((dp[i - 2][j] + triangle[i - 1][j + 1]),
                                   (dp[i - 2][j + 1] + triangle[i - 1][j + 1]))
    return max(dp[-1])
