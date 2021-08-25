class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        team = list(zip(ages,scores))
        # 나이, 스코어의 페어 형태의 리스트 생성
        team.sort()
        # 일단 나이 순으로 정렬
        n = len(team)
        
        scores = [team[i][1] for i in range(n)]
        # 재정렬된 score 리스트. 이 때 score의 기준으로 정렬된 것이 아니라 age를 기준으로 정렬된 score 리스트임
        for i in range(1,n):
            for j in range(i):
                if team[i][1]>=team[j][1]: # 반복문을 통해서 나이 어린 사람보다 나이 많은 사람이 더 높은 점수를 가졌는지 확인하고 조건에 맞는다면 지금까지의 score를 합침
                    scores[i] = max(scores[i],scores[j]+team[i][1])



        return max(scores)
