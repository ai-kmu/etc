class Solution(object):
    def findDisappearedNumbers(self, nums):
        max_n = len(nums)
        nums = set(nums)
        
        val_list = set()
        for i in range(max_n):
            val_list.add(i+1)

        tmp = []
        for i in val_list:
            if i not in nums:
                tmp.append(i)
        return tmp
