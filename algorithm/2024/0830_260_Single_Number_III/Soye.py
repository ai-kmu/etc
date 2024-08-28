class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        for i in set(nums):
            if len(res)<=2:
                if nums.count(i)==1:
                    res.append(i)
            else:
                break
        return res
