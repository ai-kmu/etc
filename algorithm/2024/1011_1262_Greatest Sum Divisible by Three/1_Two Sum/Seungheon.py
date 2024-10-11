class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tmp_list = [] # [(index, val)]

        for i, num in enumerate(nums):
            
            for tmp_num in tmp_list:
                if tmp_num[1] + num  == target:
                    return [tmp_num[0], i]
            tmp_list.append((i, num))
