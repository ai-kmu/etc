class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores) 
        list_ = []
        for i in range(n): ## ages와 scores를 한 쌍으로 리스트에 추가
            list_.append((ages[i],scores[i]))
        list_.sort(key=lambda x:(x[0],x[1])) ## age 오름차순으로 정렬
        buffer = [0]*n ## 점수 합산 저장용 버퍼
        ##나이가 같은 경우 충돌이 생기지 않기 때문에 그대로 loop 진행 가능
        for i in range(n): ## 나이가 적은 순서대로 loop진행
            score_i = list_[i][1]  
            buffer[i] = score_i ##버퍼에 현재 사람 점수를 넣는다
            for j in range(i): ## 현재 i번째 사람보다 나이가 더 적은 사람들만 loop진행
                score_j = list_[j][1] ## 현재 i번째 사람보다 나이가 적은 사람의 점수
                if score_j<=score_i: ## 나이가 적은 사람이 나이가 많은 사람보다 점수가 더 작은 경우
                    buffer[i] = max(buffer[i],buffer[j]+score_i) ## 현재 합산 값보다 이전 합산 값+ 현재 사람 점수가 더 큰 경우, 이전 합산값 + 현재 사람 점수를 현재 합산값에 반영   
        return max(buffer) ## 합산된 값 중 가장 큰 값을 선택
