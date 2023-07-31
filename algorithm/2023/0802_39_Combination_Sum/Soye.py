from itertools import combinations_with_replacement

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def rec(start, target, tmp):
            if target < 0:
                return
            if target == 0: # target이 0이라는 것은 현재 tmp의 원소를 다 더했을 때 target이 된다는 의미
                ans.append(tmp)
                return 

            for i in range(start, len(candidates)):
                rec(i, target-candidates[i], tmp + [candidates[i]])
        
        rec(0, target, [])

        return ans
