class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # age와 score에 따라 정렬
        ages_with_score = sorted(zip(ages, scores), key=lambda x: (x[0], x[1]))
        
        n = len(scores)
        dp = [0] * n 
        
        for i in range(n):
            # 나이순으로 정렬한 후 i번째 사람에서의 dp[i]는 자신의 score로 초기화
            dp[i] = ages_with_score[i][1]
            # 자신보다 나이가 작거나 같은 사람에 대해서
            for j in range(i):
                # 만약 j번째 사람보다 자신이 score가 높을 경우
                if ages_with_score[i][1] >= ages_with_score[j][1]:
                    # "dp[j] + 자신의 score"가 기존 dp[i]보다 높을 경우 업데이트
                    # "dp[j] + 자신의 score"란 j번째 사람을 기준으로 만든 팀에 i번째 사람이 참여하는 것을 의미
                    dp[i] = max(dp[i], dp[j] + ages_with_score[i][1])
        
        return max(dp)
