class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        de = {}

        for i in range(1, len(nums)+1):  
            de[i] = 0
        for i in nums:
            de[i] += 1

        ans = []
        for key, val in de.items():
            if val == 0:
                ans.append(key)
        return ans
    
