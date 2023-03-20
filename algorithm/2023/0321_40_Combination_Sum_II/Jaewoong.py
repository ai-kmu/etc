# 풀이 실패
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        res = [] # 결과 저장

        def backtrack(cur, pos, target): #cur: current combination, i: index
            if target == 0: # reach basecase
                res.append(cur.copy()) # cur 는 업데이트되는 값이기 때문에 copy를 사용
            if target <= 0:
                return
            for i in range(pos, len(candidates)):
                cur.append(candidates[i])
                # 현재 combination을 업데이트
                # 남은 candidate에서 업데이트 하기 위해 i+1
                # target을 만족하는지 확인하기 위해 계속 뺌.(0이 되면 종료)
                backtrack(cur, i + 1, target - candidates[i]) 
        backtrack([], 0, target)
        return res
