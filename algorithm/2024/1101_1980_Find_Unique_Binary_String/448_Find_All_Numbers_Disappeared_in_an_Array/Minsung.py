class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = dict()
        for i in nums:
            counter[i] = True
        ans = list()
        for i in range(1, len(nums)+1):
            try: counter[i]
            except: ans.append(i)
        return ans
