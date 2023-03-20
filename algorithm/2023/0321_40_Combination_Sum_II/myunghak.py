class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, comb, res):
            if target == 0:
                res.append(list(comb))
                return
            elif target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                backtrack(i + 1, target - candidates[i], comb, res)
                comb.pop()
        
        candidates.sort()
        res = []
        backtrack(0, target, [], res)
        return res
