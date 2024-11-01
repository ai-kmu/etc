class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        table = set(range(1,len(nums)+1))
        table2 = set(nums)

        return list(table-table2)
