def solution(triangle):
    answer = 0
    
    m = len(triangle)
    # dp table 생성
    dp = [[0 for i in range(j+1)] for j in range(m)]
    # 0,0 업데이트
    dp[0][0] = triangle[0][0]
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]

    # 1,0 부터 돌면서 업데이트
    for i in range(2, m):
        for j in range(len(triangle[i])):
            # 처음이면 이전층의 첫번째 값을 더해줌
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            # 마지막 값이면 이전층의 마지막값에 더해줌
            elif j == (len(triangle[i])-1):
                dp[i][j] = dp[i-1][-1] + triangle[i][j]
            # 사이값 이면 이전층의 이전값+지금, 이전층의 지금값+지금 중에 맥스를 넣어줌
            else:
                dp[i][j] = max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j])
                
    # 맥스 리턴
    return max(dp[-1])
