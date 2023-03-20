class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort() # 정렬해놓음

        ans = [] # 정답 리스트

        def backtracking(c, ans, tmp, t): # 재귀 구현
            
            if t == 0: # 만약 타겟에 도달하면 정답 리스트에 저장하고 리턴
                ans.append(list(tmp))
                return 

            for i in range(len(c)): # 남아있는 후보군을 쭉 돌건데
                if i > 0 and c[i] == c[i-1]: # i-1 이라는 인덱스 때문에 0 이상부터 검사하면 되는데 
                                             # 만약 겹치는 것이 있다면 우선 뒤에 있는 것부터 처리할 예정 
                    continue

                if c[i] > t: # 만약 타겟값보다 큰 값이라면 더 이상 for문을 돌 필요 없음
                    break
                
                tmp.append(c[i]) # 임시 배열에다가 저장해줌
                backtracking(c[i+1:], ans, tmp, t - c[i])
                # 이미 c[i]는 처리했으므로, c[i+1:] 을 재귀 함수의 candidates로 넣어줌
                # 정렬을 해놨기 때문에 가능한 것
                tmp.pop()

        backtracking(candidates, ans, [], target)

        return ans
