import itertools

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        new = []
        for _ in candidates:
            if _ <= target:
                new.append(_)
        print(new)
        for b in range(len(new)):
            a = itertools.combinations(new, b+1)
            for _ in a:
                if sum(_) == target:
                    ans.append(_)
        return set(ans)
