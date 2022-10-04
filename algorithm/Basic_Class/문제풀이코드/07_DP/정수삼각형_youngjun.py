def solution(triangle):
    
    # memoization 위해 dp 초기화
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    
    # 초기항 설정
    dp[0][0] = triangle[0][0]
    
    # 순환하면서 dp 채움
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            # 왼쪽 가장자리일 때
            if j == 0:
                # 대각선 위 오른쪽 항까지의 합과 현재 항을 더해준다
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            # 오른쪽 가장자리일 때
            elif i == j:
                # 대각선 위 왼쪽 항까지의 합과 현재 항을 더해준다
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            # 사이에 있을 때
            else:
                # 대각선 위 오른쪽 항까지의 합, 대각선 위 왼쪽 항까지의 합 중 큰 것과 현재 항을 더해준다.
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    
    # 전부 계산하고 dp의 마지막 list에서 가장 큰 것이 곧 거쳐간 숫자의 합이 최대값인 것이다.
    answer = max(dp[-1])
    
    return answer
