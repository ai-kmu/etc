'''
candidates를 정렬 후 백트래킹을 이용
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def backtrack(start, target, path):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # 불가능한 경우
                if candidates[i] > target:
                    break
                backtrack(i+1, target-candidates[i], path+[candidates[i]])
        backtrack(0, target, [])
        return res
