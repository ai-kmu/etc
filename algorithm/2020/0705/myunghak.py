import copy

class Solution:
    def find132pattern(self, nums) -> bool:
        start_index = 0
        max_index = len(nums)
        if max_index < 3:
            return False
        min_num = nums[0]
        max_num = nums[0]
        range_arr = [[min_num, max_num]]
        range_arr_index = 0
        while True:
            try:
                start_index +=1
                if nums[start_index] > max_num:
                    max_num = nums[start_index]
                    range_arr[range_arr_index] = [min_num, max_num]
                elif nums[start_index] < min_num:
                    min_num = nums[start_index]
                    max_num = nums[start_index]
                    range_arr.append(copy.deepcopy([min_num, max_num]))
                    range_arr_index+=1
                for mi, ma in range_arr:
                    if mi < nums[start_index] < ma:
                        return True
            except IndexError:
                return False
        
