class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # 서로 다른 수로 이루어진 배열과 Target 주어짐
        # 이 숫자들을 바탕으로 Target을 만들 수 있는 지?

        candidates.sort()
        answer = []

        # target값으로부터 하나씩 빼가면서 0을 만드는 과정으로 수행
        # current_sub는 target으로부터 현재까지 차감된 수를 의미

        def dfs(current_sub, idx, past):

            if current_sub < 0: # 차감했을 때 0보다 작으면 그냥 리턴
                return

            if current_sub == 0: # 차감했을 때 맞아떨어지면 정답
                answer.append(past)
                return

            for i in range(idx, len(candidates)): # 재귀를 돌면서, 확인. past + candidate로 현재까지 차감해온 숫자 저장
                dfs(current_sub - candidates[i], i, past + [candidates[i]])
        
        dfs(target, 0, [])

        return answer
