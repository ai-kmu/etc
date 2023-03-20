#  답보고 풀었습니다. 풀이 안해주셔도 되요

from collections import deque

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target):
            if target == 0:
                result.append(list(dq))
                return
                
            for i in range(start, len(candidates)):
                if target < candidates[i]:
                    break
                elif i <= start or candidates[i] != candidates[i-1]:
                    dq.append(candidates[i])
                    backtrack(i+1, target-candidates[i])
                    dq.pop()
                
        candidates.sort()
        dq = deque()
        result = []
        backtrack(0, target)
        return result
