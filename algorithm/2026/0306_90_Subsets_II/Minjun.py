# 조합 이용해서 풀었음. 쉬워서 주석생략
import itertools
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        st = 1
        while st <= len(nums):
            a = list(itertools.combinations(nums, st))
            for b in a:
                b = list(b)
                b.sort()
                if b not in ans:
                    ans.append(b)
            st += 1
        return ans
