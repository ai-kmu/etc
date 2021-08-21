class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #DP
        n = len(scores)
        mergedList = [[0 for col in range(2)] for row in range(n)] 

        for i in range(n):                  #정렬하기 위해 n*2 리스트로 병합
            mergedList[i][0] = scores[i]
            mergedList[i][1] = ages[i]

        mergedList.sort(key = lambda x:(x[1], x[0]))    #age ascending -> score ascending 순으로 정렬
        
        dp = [0 for i in range(n)]                      #i번째 항에서의 sum of score
        sum = 0
        
        for i in range(n):
            score = mergedList[i][0]                    #i번째 항에서의 score
            dp[i] = score                               #dp[i]가 한번도 갱신되지 않은 경우 고려

            for j in range(i):                          
                if mergedList[i][0] >= mergedList[j][0]:    #age와 score 모두 i번째 항보다 작은 모든 j에 대하여
                    dp[i] = max(dp[i], dp[j] + score)       #sum_of_score_at(j) + score의 최대값 = dp[i] 

            sum = max(sum, dp[i])                       #dp[i]의 최대값
            
        return sum

        
