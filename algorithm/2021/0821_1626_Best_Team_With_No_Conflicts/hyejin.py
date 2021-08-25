class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        answer = 0
        
        # age와  score을 같이 정렬하고, 해당 age 위치의 score와 / 비교하는 age의 score + 해당 age의 score 비교 => 계속 update
        # sorting을 descending보다 ascending로 하는게 dp에 적합..
        sort_ages = sorted(zip(ages, scores))
        # sum을 저장할 array
        score_sum = [0 for _ in range(len(scores))]
        
        # ascending으로 array 채워나감
        for i in range(len(scores)):
            score_sum[i] = sort_ages[i][1]
            for j in range(i): # 0~i까지 i와 비교하면서 update하면됨.
                if sort_ages[j][1] <= sort_ages[i][1]: # 현재 나이보다 작거나 같은데 i의 score가 더 크면 j를 넣을 수 있음.
                    score_sum[i] = max(score_sum[i], score_sum[j] + sort_ages[i][1])
        
        return max(score_sum)
