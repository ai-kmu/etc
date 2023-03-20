class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        # backtracking 방법 사용을 위한 함수 생성
        def backtracking(start_ind,comb,ans):
            if sum(comb) == target:
                ans.append(comb)
                return

            # comb 안 요소값 합할 때 target보다 크면 return으로 backtracking 함수 종료
            if sum(comb) > target: 
                return
            
            for i in range(start_ind,len(candidates)):
                # comb에 추가할 숫자가 target보다 크면 for문 break
                if candidates[i] > target: 
                    break

                # 중복된 comb 추가를 방지. 중복된 comb가 나오는 이유는 candidates 내에 같은 값 요소가 들어있기 때문
                if i > start_ind and candidates[i] == candidates[i-1]:
                    continue
                    
                backtracking(i+1,comb+[candidates[i]],ans)

        backtracking(0,[],ans)
        
        return ans
