# itertools 사용
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)+1):
            ans += list(combinations(nums,i)) 
        return list(set(ans))
