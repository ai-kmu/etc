# 수학적으로 풀어보다가 막힘

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        s = 0
        cnt = 0
        
        # 최대 개수
        for i in range(len(candidates)):
            maximum = target // candidates[i]

            a = [candidates[i]] * maximum
            if not a:
                return []

            for j in candidates:
                a.pop()
                a.append(j)
                if sum(a) == target:
                    a.sort()
                    ans.add(tuple(a[:]))

        return list(ans)
