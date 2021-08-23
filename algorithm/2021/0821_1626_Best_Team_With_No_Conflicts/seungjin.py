def bestTeamscore(scores , ages):
    arr = sorted(zip(ages , scores) , reverse= True)
    dp = [0]* len(arr)
    for i in range(len(arr)):
        dp[i] = arr[i][1] #score가 들어있음
        for j in range(i):
            if arr[j][1] >= arr[i][1]: #나이도 많고 점수도 높은경우
                dp[i] = max(dp[i] , dp[j]+ arr[i][1])
                #나 자신의 점수와 이전최대 점수와 나자신을 더한것을
                #제일 큰것을 찾는다.
    return max(dp)
