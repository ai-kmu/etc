class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #age와 스코어를 묶어서 리스트로 만들어준다.
        for i in range(len(ages)):
            team=list(zip(ages,scores))
    
        # 나이를 오름차순으로 정렬한다
        team.sort()
        
        # 스코어를 계산할 리스트를 만든다
        score=[0 for i in scores]
        
        for i in range(len(scores)):
            #현재 선수의 스코어를 score에 넣어준다
            score[i]=team[i][1]
            for j in range(i):
                # 만약 현재 더 나이가 어리거나 같은 선수가 score가 높을 경우
                if(team[i][1]>=team[j][1]):
                    # score에 i번째 선수의 score값과 j번째 선수의 score값을 합하여 score i에 넣어준다
                    score[i]=max(score[i],score[j]+team[i][1])
                    
        # score값 중 가장 큰 수를 반환하여 점수를 모두 더한 값을 반환한다.            
        return max(score);
